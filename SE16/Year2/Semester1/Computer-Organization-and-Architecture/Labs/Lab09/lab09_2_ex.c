#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/i2c-dev.h>
#include <gpiod.h>
#include <stdbool.h>

#define BMP280_ADDR 0x76   // Change to 0x77 if needed
#define OLED_ADDR  0x3C
#define I2C_DEV    "/dev/i2c-1"
#define WIDTH      128
#define GPIOCHIP   "/dev/gpiochip0"
#define BTN_GPIO   25

static int i2c_fd = -1;
static struct gpiod_chip *chip = NULL;
static struct gpiod_line *btn  = NULL;
static volatile int running = 1;
static bool is_celsius = true;

static void on_sigint(int sig){ (void)sig; running = 0; }
static void die(const char *msg){ perror(msg); exit(1); }

//////////////////////////
// I2C helpers
//////////////////////////
static void i2c_set_addr(int addr){
  if(ioctl(i2c_fd, I2C_SLAVE, addr) < 0) die("I2C_SLAVE");
}

static void i2c_write_buf(const uint8_t *buf, size_t n){
  if(write(i2c_fd, buf, n) != (ssize_t)n) die("i2c write");
}

static int i2c_write_byte(uint8_t reg, uint8_t val){
  uint8_t b[2] = {reg,val};
  return (write(i2c_fd, b,2)==2)?0:-1;
}

static int i2c_read_buf(uint8_t reg, uint8_t *buf, int len){
  if(write(i2c_fd, &reg,1)!=1) return -1;
  if(read(i2c_fd, buf,len)!=len) return -1;
  return 0;
}

//////////////////////////
// OLED
//////////////////////////
static void oled_cmd(uint8_t c){
  uint8_t b[2] = {0x00, c};
  i2c_set_addr(OLED_ADDR);
  i2c_write_buf(b,2);
}

static void oled_data(const uint8_t *data, size_t n){
  uint8_t b[1+128];
  if(n>128) n=128;
  b[0]=0x40;
  memcpy(&b[1], data,n);
  i2c_set_addr(OLED_ADDR);
  i2c_write_buf(b,n+1);
}

static void oled_set_cursor(int x,int page){
  oled_cmd(0xB0 + (page&7));
  oled_cmd(0x00 + (x &0x0F));
  oled_cmd(0x10 + ((x>>4)&0x0F));
}

static void oled_init(){
  oled_cmd(0xAE); // OFF
  oled_cmd(0x20); oled_cmd(0x02); // page mode
  oled_cmd(0xA8); oled_cmd(0x3F); // multiplex
  oled_cmd(0xD3); oled_cmd(0x00); // display offset
  oled_cmd(0x40); // start line
  oled_cmd(0xA1); // segment remap
  oled_cmd(0xC8); // COM scan dec
  oled_cmd(0xDA); oled_cmd(0x12); // COM pins
  oled_cmd(0x81); oled_cmd(0x7F); // contrast
  oled_cmd(0xA4); // display all on resume
  oled_cmd(0xA6); // normal display
  oled_cmd(0xD5); oled_cmd(0x80); // osc freq
  oled_cmd(0x8D); oled_cmd(0x14); // charge pump
  oled_cmd(0xAF); // ON
}

static void oled_clear(){
    uint8_t zero[WIDTH]; memset(zero,0,sizeof(zero));
    for(int p=0;p<8;++p){ oled_set_cursor(0,p); oled_data(zero,WIDTH); }
}

//////////////////////////
// Font (5x7)
//////////////////////////
static const uint8_t G_SPACE[5]={0,0,0,0,0};
static const uint8_t G_T[5]={0x7F,0x08,0x08,0x08,0x08};
static const uint8_t G_e[5]={0x3E,0x49,0x49,0x49,0x26};
static const uint8_t G_m[5]={0x7F,0x04,0x18,0x04,0x7F};
static const uint8_t G_p[5]={0x7F,0x12,0x12,0x12,0x0C};
static const uint8_t G_semi[5]={0x00,0x36,0x36,0x00,0x00};
static const uint8_t G_C[5]={0x3E,0x41,0x41,0x41,0x22};
static const uint8_t G_F[5]={0x7F,0x09,0x09,0x09,0x01};
static const uint8_t G_0[5]={0x3E,0x51,0x49,0x45,0x3E};
static const uint8_t G_1[5]={0x00,0x42,0x7F,0x40,0x00};
static const uint8_t G_2[5]={0x42,0x61,0x51,0x49,0x46};
static const uint8_t G_3[5]={0x21,0x41,0x45,0x4B,0x31};
static const uint8_t G_4[5]={0x18,0x14,0x12,0x7F,0x10};
static const uint8_t G_5[5]={0x27,0x45,0x45,0x45,0x39};
static const uint8_t G_6[5]={0x3C,0x4A,0x49,0x49,0x30};
static const uint8_t G_7[5]={0x01,0x71,0x09,0x05,0x03};
static const uint8_t G_8[5]={0x36,0x49,0x49,0x49,0x36};
static const uint8_t G_9[5]={0x06,0x49,0x49,0x29,0x1E};

static const uint8_t* glyph(char c){
  switch(c){
    case ' ': return G_SPACE;
    case 'T': return G_T;
    case 'e': return G_e;
    case 'm': return G_m;
    case 'p': return G_p;
    case ':': return G_semi;
    case 'C': return G_C;
    case 'F': return G_F;
    case '0': return G_0;
    case '1': return G_1;
    case '2': return G_2;
    case '3': return G_3;
    case '4': return G_4;
    case '5': return G_5;
    case '6': return G_6;
    case '7': return G_7;
    case '8': return G_8;
    case '9': return G_9;
    default: return G_SPACE;
  }
}

static void oled_char(int x,int page,char ch){
  const uint8_t* g = glyph(ch);
  oled_set_cursor(x,page); oled_data(g,5);
  uint8_t sp=0; oled_data(&sp,1);
}

static void oled_text(int x,int page,const char* s){
  while(*s && page<8){
    if(x+6>WIDTH){ x=0; page++; continue; }
    oled_char(x,page,*s++);
    x+=6;
  }
}

//////////////////////////
// Button (switch C/F)
//////////////////////////
static void gpio_init(){
  chip = gpiod_chip_open(GPIOCHIP);
  if(!chip) die("gpiod_chip_open");
  btn = gpiod_chip_get_line(chip,BTN_GPIO);
  if(!btn) die("gpiod_chip_get_line");
  if(gpiod_line_request_input_flags(btn,"btn",GPIOD_LINE_REQUEST_FLAG_BIAS_PULL_UP)<0)
    die("gpiod_line_request_input_flags");
}

static void check_button(){
  static int last_val = 1;
  int v = gpiod_line_get_value(btn);
  if(last_val==1 && v==0){ // pressed (active low)
    is_celsius = !is_celsius;
    usleep(30000); // debounce
  }
  last_val=v;
}

//////////////////////////
// BMP280
//////////////////////////
#define REG_CALIB_START 0x88
#define REG_ID 0xD0
#define REG_CTRL_MEAS 0xF4
#define REG_CONFIG 0xF5
#define REG_PRESS_MSB 0xF7

static uint16_t dig_T1; static int16_t dig_T2,dig_T3;

static void bmp280_init_and_calib(void){
  uint8_t id=0;
  i2c_set_addr(BMP280_ADDR);
  if(i2c_read_buf(REG_ID,&id,1)<0) die("read ID");
  if(id!=0x58) fprintf(stderr,"Warning: BMP280 ID=0x%02X\n",id);

  uint8_t calib[6];
  if(i2c_read_buf(REG_CALIB_START,calib,6)<0) die("read calib");
  dig_T1 = calib[1]<<8 | calib[0];
  dig_T2 = calib[3]<<8 | calib[2];
  dig_T3 = calib[5]<<8 | calib[4];

  if(i2c_write_byte(REG_CONFIG,0x80)<0) die("write CONFIG");
  if(i2c_write_byte(REG_CTRL_MEAS,(1<<5)|(1<<2)|0x03)<0) die("write CTRL_MEAS");
}

static int read_temp(float *out){
  uint8_t raw[3];
  i2c_set_addr(BMP280_ADDR);
  if(i2c_read_buf(REG_PRESS_MSB+3, raw,3)<0) return -1; // temp MSB=F7+3=FA
  int32_t adc_T = (raw[0]<<12)|(raw[1]<<4)|(raw[2]>>4);
  int32_t var1 = ((((adc_T>>3)-((int32_t)dig_T1<<1)))*((int32_t)dig_T2))>>11;
  int32_t var2 = (((((adc_T>>4)-((int32_t)dig_T1))*((adc_T>>4)-((int32_t)dig_T1)))>>12)*((int32_t)dig_T3))>>14;
  int32_t t_fine = var1 + var2;
  *out = (t_fine*5 +128)/25600.0f;
  return 0;
}

//////////////////////////
// Main
//////////////////////////
int main(){
  signal(SIGINT,on_sigint);

  i2c_fd = open(I2C_DEV,O_RDWR);
  if(i2c_fd<0) die("open i2c");

  oled_init();
  oled_clear();
  gpio_init();
  bmp280_init_and_calib();

  while(running){
    check_button();
    float T_C;
    if(read_temp(&T_C)==0){
      char text[32];
      float display_temp = is_celsius? T_C : T_C*9/5 +32;
      snprintf(text,sizeof(text),"Temp: %.2f %c", display_temp, is_celsius?'C':'F');
      oled_clear();
      oled_text(0,0,text);
    } else {
      fprintf(stderr,"Read error\n");
    }
    sleep(2);
  }

  close(i2c_fd);
  return 0;
}

