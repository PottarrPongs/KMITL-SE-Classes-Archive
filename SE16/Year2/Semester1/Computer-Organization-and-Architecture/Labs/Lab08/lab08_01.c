#include <stdio.h>
#include <pigpio.h>

#define LED_PIN 18

int main() {
  if (gpioInitialise() < 0) {
    printf("pigpio init failed\n");
    return 1;
  }
  gpioSetMode(LED_PIN, PI_OUTPUT);
  while (1) {
    gpioWrite(LED_PIN, 1);
    gpioDelay(500000);
    gpioWrite(LED_PIN, 0);
    gpioDelay(500000);
  }
  gpioTerminate();
  return 0;
}
