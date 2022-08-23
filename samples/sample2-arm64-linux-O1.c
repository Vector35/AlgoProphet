#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double get_pythagorean(double a, double b) {
	double square_sum = a * a + b * b;
	return sqrt(square_sum);
}

int get_midvalue(int a, int b) {
	int midval = (a + b) / 2;
	return midval;
}

int get_percentage(int a, int b) {
	int res = (a / b) * 100;
	return res;
}

int main() {
	printf("hello\n");
}
