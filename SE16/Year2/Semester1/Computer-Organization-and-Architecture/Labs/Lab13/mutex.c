#include <stdio.h>
#include <pthread.h>
#include <stdint.h>

typedef int64_t cents_t;
static cents_t balance = 100000;
static pthread_mutex_t mtx = PTHREAD_MUTEX_INITIALIZER;

static void* deposit(void* arg) {
  const cents_t amt = *(const cents_t*)arg;
  cents_t snap;
  pthread_mutex_lock(&mtx);
  balance += amt;
  snap = balance;
  pthread_mutex_unlock(&mtx);
  printf("Deposit $%.2f. New balance: $%.2f\n", amt/100.0, snap/100.0);
  return NULL;
}

static void* withdraw(void* arg) {
  const cents_t amt = *(const cents_t*)arg;
  cents_t snap;
  pthread_mutex_lock(&mtx);
  if (balance >= amt) {
    balance -= amt;
  }
  snap = balance;
  pthread_mutex_unlock(&mtx);
  printf("Withdraw $%.2f. New balance: $%.2f\n", amt/100.0, snap/100.0);
  return NULL;
}

int main(void){
  pthread_t t1, t2;
  cents_t dep = 50000;
  cents_t wd = 20000;

  if (pthread_create(&t1, NULL, deposit, &dep) != 0) { perror("pthread_create"); return 1; }
  if (pthread_create(&t2, NULL, withdraw, &wd) != 0) { perror("pthread_create"); return 1; }
  if (pthread_join(t1, NULL)) { perror("pthread_join"); return 1; }
  if (pthread_join(t2, NULL)) { perror("pthread_join"); return 1; }

  printf("Finall balnce: $%.2f\n", balance/100.0);
  return 0;
}
