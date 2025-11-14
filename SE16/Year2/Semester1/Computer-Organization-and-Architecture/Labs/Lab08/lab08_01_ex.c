#include <stdio.h>
#include <pigpio.h>

#define LED_PIN_YELLOW 24
#define LED_PIN_RED 23
#define LED_PIN_BLUE 18

int main() {
  if (gpioInitialise() < 0) {
    printf("pigpio init failed\n");
    return 1;
  }
  gpioSetMode(LED_PIN_YELLOW, PI_OUTPUT);
  gpioSetMode(LED_PIN_RED, PI_OUTPUT);
  gpioSetMode(LED_PIN_BLUE, PI_OUTPUT);
  while (1) {
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
      gpioDelay(500000);
    }
  }
  gpioTerminate();
  return 0;
}
