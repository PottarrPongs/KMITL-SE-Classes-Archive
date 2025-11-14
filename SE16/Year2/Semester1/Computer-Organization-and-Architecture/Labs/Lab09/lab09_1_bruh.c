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

/* --- Config --- */
#define I2C_DEV   "/dev/i2c-1"
#define OLED_ADDR 0x3C
#define WIDTH     128
#define GPIOCHIP  "/dev/gpiochip0"
#define BTN_GPIO  25

static int i2c_fd = -1;
static struct gpiod_chip *chip = NULL;
static struct gpiod_line *btn  = NULL;
static volatile int running = 1;
static void on_sigint(int sig){ (void)sig; running = 0; }

/* --- I2C helpers --- */
static inline void die(const char* msg){ perror(msg); exit(1); }
static void i2c_set_addr(int addr){
    if (ioctl(i2c_fd, I2C_SLAVE, addr) < 0) die("I2C_SLAVE");
}
static void i2c_write_buf(const uint8_t *buf, size_t n){
    if (write(i2c_fd, buf, n) != (ssize_t)n) die("i2c write");
}

/* --- OLED --- */
static void oled_cmd(uint8_t c){
    uint8_t b[2] = {0x00, c};
    i2c_set_addr(OLED_ADDR); i2c_write_buf(b, 2);
}
static void oled_data(const uint8_t *data, size_t n){
    uint8_t b[1+128];
    if (n > 128) n = 128;
    b[0] = 0x40;
    memcpy(&b[1], data, n);
    i2c_set_addr(OLED_ADDR); i2c_write_buf(b, n+1);
}
static void oled_set_cursor(int x, int page){
    oled_cmd(0xB0 + (page & 7));
    oled_cmd(0x00 + (x & 0x0F));
    oled_cmd(0x10 + ((x >> 4) & 0x0F));
}
static void oled_init(){
    oled_cmd(0xAE);
    oled_cmd(0x20); oled_cmd(0x02);
    oled_cmd(0xA8); oled_cmd(0x3F);
    oled_cmd(0xD3); oled_cmd(0x00);
    oled_cmd(0x40);
    oled_cmd(0xA1);
    oled_cmd(0xC8);
    oled_cmd(0xDA); oled_cmd(0x12);
    oled_cmd(0x81); oled_cmd(0x7F);
    oled_cmd(0xA4);
    oled_cmd(0xA6);
    oled_cmd(0xD5); oled_cmd(0x80);
    oled_cmd(0x8D); oled_cmd(0x14);
    oled_cmd(0xAF);
}
static void oled_clear(){
    uint8_t zero[WIDTH]; memset(zero,0,sizeof(zero));
    for(int p=0;p<8;++p){ oled_set_cursor(0,p); oled_data(zero,WIDTH); }
}
static void oled_clear_line(int page){
    uint8_t zero[WIDTH]; memset(zero,0,sizeof(zero));
    oled_set_cursor(0,page); oled_data(zero,WIDTH);
}

/* --- Minimal font: only needed glyphs --- */
/* 5x7 font, each glyph = 5 columns, LSB = top */
static const uint8_t G_SPACE[5]={0,0,0,0,0};
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

static const uint8_t G_R[5]={0x7F,0x09,0x19,0x29,0x46};
static const uint8_t G_P[5]={0x7F,0x09,0x09,0x09,0x06};

static const uint8_t G_a[5]={0x20,0x54,0x54,0x54,0x78};
static const uint8_t G_b[5]={0x7F,0x48,0x44,0x44,0x38};
static const uint8_t G_e[5]={0x38,0x54,0x54,0x54,0x18};
static const uint8_t G_h[5]={0x7F,0x08,0x04,0x04,0x78};
static const uint8_t G_i[5]={0x00,0x44,0x7D,0x40,0x00};
static const uint8_t G_l[5]={0x00,0x41,0x7F,0x40,0x00};
static const uint8_t G_o[5]={0x38,0x44,0x44,0x44,0x38};
static const uint8_t G_p[5]={0x7C,0x14,0x14,0x14,0x08};
static const uint8_t G_r[5]={0x7C,0x08,0x04,0x04,0x08};
static const uint8_t G_s[5]={0x48,0x54,0x54,0x54,0x24};
static const uint8_t G_y[5]={0x0C,0x50,0x50,0x50,0x3C};

/* Map only the characters we support */
static const uint8_t* glyph(char c){
    switch(c){
        case ' ': return G_SPACE;
        case '0': return G_0; case '1': return G_1; case '2': return G_2; case '3': return G_3;
        case '4': return G_4; case '5': return G_5; case '6': return G_6; case '7': return G_7;
        case '8': return G_8; case '9': return G_9;
        case 'R': return G_R; case 'P': return G_P;
        case 'a': return G_a; case 'b': return G_b; case 'e': return G_e; case 'h': return G_h;
        case 'i': return G_i; case 'l': return G_l; case 'o': return G_o; case 'p': return G_p;
        case 'r': return G_r; case 's': return G_s; case 'y': return G_y;
        default:  return G_SPACE; // any unsupported char -> blank
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
        oled_char(x,page,*s++); x+=6;
    }
}

/* --- Button (libgpiod) --- */
static void gpio_init(){
    chip = gpiod_chip_open(GPIOCHIP);
    if(!chip) die("gpiod_chip_open");
    btn = gpiod_chip_get_line(chip, BTN_GPIO);
    if(!btn) die("gpiod_chip_get_line");
    if(gpiod_line_request_input_flags(btn,"btn",GPIOD_LINE_REQUEST_FLAG_BIAS_PULL_UP)<0)
        die("gpiod_line_request_input_flags");
}
static void wait_button(){
    int last=gpiod_line_get_value(btn);
    while(running){
        usleep(5000);
        int v=gpiod_line_get_value(btn);
        if(last==1 && v==0){ // pressed (active-low)
            usleep(30000); // debounce
            while(gpiod_line_get_value(btn)==0) usleep(10000); // wait release
            return;
        }
        last=v;
    }
}

/* --- Main state machine --- */
int main(){
    signal(SIGINT,on_sigint);
    i2c_fd=open(I2C_DEV,O_RDWR); if(i2c_fd<0) die("open i2c");
    oled_init(); oled_clear();
    gpio_init();

    int state=0;
    while(running){
        if(state==0){
            oled_clear();
            oled_text(0,0,"hello");          // uses h,e,l,o
            wait_button(); state=1;
        }
        else if(state==1){
            oled_clear_line(1);
            oled_text(0,1,"Raspberry Pi");  // uses R,a,s,p,b,e,r,y, space, P,i
            wait_button(); state=2;
        }
        else if(state==2){
            oled_clear_line(1);
            oled_text(0,1,"0123456789");    // digits 0–9
            wait_button(); state=3;
        }
        else{
            oled_clear();                   // back to start
            wait_button(); state=0;
        }
    }
    if(btn) gpiod_line_release(btn);
    if(chip) gpiod_chip_close(chip);
    if(i2c_fd>=0) close(i2c_fd);
    return 0;
}
