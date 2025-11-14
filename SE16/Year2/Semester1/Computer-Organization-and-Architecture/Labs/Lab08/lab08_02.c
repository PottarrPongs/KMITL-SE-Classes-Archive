#include <stdio.h>
#include <pigpio.h>

#define LED_PIN 18
#define BTN_PIN 25

int main() {
  if (gpioInitialise() < 0) {
    printf("pigpio init failed\n");
    return 1;
  }
  gpioSetMode(LED_PIN, PI_OUTPUT);
  gpioSetMode(BTN_PIN, PI_INPUT);
  gpioSetPullUpDown(BTN_PIN, PI_PUD_UP);
  int led_state = 0;
  int last_state = 1;

  while (1) {
    int btn_state = gpioRead(BTN_PIN);
    if (last_state == 1 && btn_state == 0) {
      led_state = !led_state;
      gpioWrite(LED_PIN, led_state);
      gpioDelay(200000);
    }
    last_state = btn_state;
    gpioDelay(1000);
  }
  gpioTerminate();
  return 0;
}
