#include <stdio.h>
#include <stdbool.h>
#include <pigpio.h>
#include <pigpio.h>

#define LED_PIN_YELLOW 24
#define LED_PIN_RED 23
#define LED_PIN_BLUE 18
#define BTN_PIN 25

int main() {

  int spd[3] = {200000, 500000, 1000000};
  bool is_forward = true;
  bool is_auto_run = true;
  bool is_reverse = false;

  if (gpioInitialise() < 0) {
    printf("pigpio init failed\n");
    return 1;
  }
  gpioSetMode(LED_PIN_YELLOW, PI_OUTPUT);
  gpioSetMode(LED_PIN_RED, PI_OUTPUT);
  gpioSetMode(LED_PIN_BLUE, PI_OUTPUT);
  gpioSetMode(BTN_PIN, PI_INPUT);
  gpioSetPullUpDown(BTN_PIN, PI_PUD_UP);
  int n = 0;
  int count = 0;
  int last_state = 1;
  int btn_state;
  while (1) {
    if (!is_auto_run) {
      while (1) {
        printf("BTN %d\n", btn_state);
        count = 0;
        last_state = btn_state;
        gpioDelay(10000);
        btn_state = gpioRead(BTN_PIN);
        if (last_state == 1 && btn_state == 0) {
          count++;
        }
        last_state = btn_state;
        gpioDelay(10000);
        if (last_state == 1 && btn_state == 0) {
          count++;
        }
        last_state = btn_state;
        gpioDelay(10000);
        if (count == 1) {
          is_auto_run = !is_auto_run;
        } else if (count == 2) {
          is_reverse = !is_reverse;
        }
        btn_state = 1;
      }
    } else {
      btn_state = gpioRead(BTN_PIN);
      if (last_state == 1 && btn_state == 0) {
        is_auto_run = !is_auto_run;
      }
      last_state = btn_state;
      gpioDelay(10000);
      btn_state = gpioRead(BTN_PIN);
      if (last_state == 0 && btn_state == 1) {
        btn_state = gpioRead(BTN_PIN);
        gpioDelay(1000000);
      if (last_state == 0 && btn_state == 0) {
        if (n == 1) {
          n = 0;
        } else {
          n++;
        }
      }
      }

      if (!is_reverse) {
        for (int i = 0; i < 6; i++) {
          if (i < 3) {
            gpioWrite(LED_PIN_YELLOW, 0);
          } else {
            gpioWrite(LED_PIN_YELLOW, 1);
          }
          if (i < 2 || i == 5) {
            gpioWrite(LED_PIN_RED, 0);
          } else {
            gpioWrite(LED_PIN_RED, 1);
          }
          if (i == 0 || i > 3) {
            gpioWrite(LED_PIN_BLUE, 0);
          } else {
            gpioWrite(LED_PIN_BLUE, 1);
          }
          gpioDelay(spd[n]);
        }
      } else {
          for (int i = 0; i < 6; i++) {
          if (i == 0 || i > 3) {
            gpioWrite(LED_PIN_YELLOW, 0);
          } else {
            gpioWrite(LED_PIN_YELLOW, 1);
          }
          if (i < 2 || i == 5) {
            gpioWrite(LED_PIN_RED, 0);
          } else {
            gpioWrite(LED_PIN_RED, 1);
          }
          if (i < 3) {
            gpioWrite(LED_PIN_BLUE, 0);
          } else {
            gpioWrite(LED_PIN_BLUE, 1);
          }
          gpioDelay(spd[n]);
        }

      }
    }
    
  }
  gpioTerminate();
  return 0;
}
