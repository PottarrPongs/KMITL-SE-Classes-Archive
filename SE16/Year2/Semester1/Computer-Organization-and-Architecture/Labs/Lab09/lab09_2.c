#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <signal.h>
#include <time.h>
#include <sys/ioctl.h>
#include <linux/i2c-dev.h>

#ifndef BMP280_ADDR
#define BMP280_ADDR 0x76       // Change to 0x77 if your module uses that address
#endif

#define I2C_DEV "/dev/i2c-1"

// BMP280 registers
#define REG_CALIB_START 0x88   // 24 bytes: dig_T1..dig_T3, dig_P1..dig_P9
#define REG_ID          0xD0   // should be 0x58
#define REG_RESET       0xE0
#define REG_STATUS      0xF3
#define REG_CTRL_MEAS   0xF4
#define REG_CONFIG      0xF5
#define REG_PRESS_MSB   0xF7   // F7..F9 pressure, FA..FC temp

static int fd = -1;
static volatile int running = 1;
static void on_sigint(int sig){ (void)sig; running = 0; }





// Compensation params
static uint16_t dig_T1; static int16_t dig_T2, dig_T3;
static uint16_t dig_P1; static int16_t dig_P2, dig_P3, dig_P4, dig_P5, dig_P6, dig_P7, dig_P8, dig_P9;

static inline void die(const char* m){ perror(m); exit(1); }

static int i2c_write_byte(uint8_t reg, uint8_t val){
    uint8_t b[2] = {reg, val};
    return (write(fd, b, 2) == 2) ? 0 : -1;
}
static int i2c_read_buf(uint8_t reg, uint8_t *buf, int len){
    if (write(fd, &reg, 1) != 1) return -1;
    if (read(fd, buf, len) != len) return -1;
    return 0;
}

static void bmp280_init_and_calib(void){
    // Optional: verify ID
    uint8_t id=0;
    if (i2c_read_buf(REG_ID, &id, 1) < 0) die("read ID");
    if (id != 0x58) {
        fprintf(stderr, "Warning: unexpected BMP280 ID 0x%02X (expected 0x58)\n", id);
    }

    // Read calibration
    uint8_t calib[24];
    if (i2c_read_buf(REG_CALIB_START, calib, 24) < 0) die("read calib");
    dig_T1 = (uint16_t)(calib[1] << 8 | calib[0]);
    dig_T2 = (int16_t) (calib[3] << 8 | calib[2]);
    dig_T3 = (int16_t) (calib[5] << 8 | calib[4]);
    dig_P1 = (uint16_t)(calib[7] << 8 | calib[6]);
    dig_P2 = (int16_t) (calib[9] << 8 | calib[8]);
    dig_P3 = (int16_t) (calib[11] << 8 | calib[10]);
    dig_P4 = (int16_t) (calib[13] << 8 | calib[12]);
    dig_P5 = (int16_t) (calib[15] << 8 | calib[14]);
    dig_P6 = (int16_t) (calib[17] << 8 | calib[16]);
    dig_P7 = (int16_t) (calib[19] << 8 | calib[18]);
    dig_P8 = (int16_t) (calib[21] << 8 | calib[20]);
    dig_P9 = (int16_t) (calib[23] << 8 | calib[22]);

    // Configure: t_sb=500ms (0x80), filter=off; osrs_t=osrs_p=1, mode=normal (0x27 or 0x23? -> osrs_t=1<<5, osrs_p=1<<2, mode=3)
    if (i2c_write_byte(REG_CONFIG, 0x80) < 0) die("write CONFIG");
    if (i2c_write_byte(REG_CTRL_MEAS, (1<<5) | (1<<2) | 0x03) < 0) die("write CTRL_MEAS");
}

static int read_tp(float *out_T_C, float *out_P_hPa){
    uint8_t raw[6];
    if (i2c_read_buf(REG_PRESS_MSB, raw, 6) < 0) return -1;

    int32_t adc_P = (int32_t)((raw[0] << 12) | (raw[1] << 4) | (raw[2] >> 4));
    int32_t adc_T = (int32_t)((raw[3] << 12) | (raw[4] << 4) | (raw[5] >> 4));

    // Temperature compensation
    int32_t var1 = ((((adc_T >> 3) - ((int32_t)dig_T1 << 1))) * ((int32_t)dig_T2)) >> 11;
    int32_t var2 = (((((adc_T >> 4) - ((int32_t)dig_T1)) * ((adc_T >> 4) - ((int32_t)dig_T1))) >> 12) * ((int32_t)dig_T3)) >> 14;
    int32_t t_fine = var1 + var2;
    float T = (t_fine * 5 + 128) / 25600.0f; // °C

    // Pressure compensation
    int64_t var1p = ((int64_t)t_fine) - 128000;
    int64_t var2p = var1p * var1p * (int64_t)dig_P6;
    var2p = var2p + ((var1p * (int64_t)dig_P5) << 17);
    var2p = var2p + (((int64_t)dig_P4) << 35);
    var1p = ((var1p * var1p * (int64_t)dig_P3) >> 8) + ((var1p * (int64_t)dig_P2) << 12);
    var1p = (((((int64_t)1) << 47) + var1p)) * ((int64_t)dig_P1) >> 33;
    if (var1p == 0) return -2; // avoid div by zero

    int64_t p = 1048576 - adc_P;
    p = (((p << 31) - var2p) * 3125) / var1p;
    var1p = (((int64_t)dig_P9) * (p >> 13) * (p >> 13)) >> 25;
    var2p = (((int64_t)dig_P8) * p) >> 19;
    p = ((p + var1p + var2p) >> 8) + (((int64_t)dig_P7) << 4);
    float P_hPa = (p / 256.0f) / 100.0f;

    *out_T_C   = T;
    *out_P_hPa = P_hPa;
    return 0;
}

int main(int argc, char **argv){
    signal(SIGINT, on_sigint);

    // Allow optional override: ./bmp280_console_10s 0x77
    int addr = BMP280_ADDR;
    if (argc >= 2) {
        addr = (int)strtol(argv[1], NULL, 0);
        if (addr < 0x03 || addr > 0x77) {
            fprintf(stderr, "Invalid I2C address: %s\n", argv[1]);
            return 1;
        }
    }

    fd = open(I2C_DEV, O_RDWR);
    if (fd < 0) die("open /dev/i2c-1");
    if (ioctl(fd, I2C_SLAVE, addr) < 0) die("I2C_SLAVE");

    bmp280_init_and_calib();

    printf("BMP280 at 0x%02X; reading every 10s. Press Ctrl-C to stop.\n", addr);

    while (running) {
        float T, P;
        int rc = read_tp(&T, &P);
        if (rc == 0) {
            time_t now = time(NULL);
            struct tm *lt = localtime(&now);
            char ts[32];
            strftime(ts, sizeof(ts), "%Y-%m-%d %H:%M:%S", lt);
            printf("[%s] Temperature: %.2f C, Pressure: %.2f hPa\n", ts, T, P);
            fflush(stdout);
        } else {
            fprintf(stderr, "Read error (%d)\n", rc);
        }
        sleep(10);
    }

    close(fd);
    return 0;
}
