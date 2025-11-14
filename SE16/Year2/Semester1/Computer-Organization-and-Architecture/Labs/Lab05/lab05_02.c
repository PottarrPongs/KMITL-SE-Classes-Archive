#include <stdio.h>

extern int add(int a, int b);

int main() {
	int x = 7, y = 5;
	int result = add(x, y);
	printf("Result %d\n", result);
	return 2;
}
