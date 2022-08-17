#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int get_area(int rad) {
	return rad * rad * M_PI;
}

int get_area_with_power(int rad) {
	return pow(rad, 2) * M_PI;
}

int get_circum(int rad) {
	return 2 * M_PI * rad;
}

int get_ball_vol(int rad) {
	return 4 / 3 * M_PI * pow(rad, 3);
}

int get_ball_surface(int rad) {
	return 4 * M_PI * pow(rad, 2);
}

int get_cylind_vol(int rad, int height) {
	return M_PI * pow(rad, 2) * height;
}

int get_cylind_surface(int rad, int height) {
	return 2 * M_PI * pow(rad, 2) + 2 * M_PI * rad * height;
}

int get_cone_vol(int rad, int height) {
	return 1/3 * M_PI * pow(rad, 2) * height;
}

int get_cone_surface(int rad, int height) {
	return M_PI * pow(rad, 2) + M_PI * rad * sqrt( pow(rad, 2) + pow(height, 2) );
}

int get_arr_average(int arr[], int size) {
	int sum = 0;
	for(int i = 0; i < size; i++) {
		sum += arr[i];
	}
	return sum / size;
}

int get_euclidean(int arr1[], int arr2[], int size) {
	// two arrays need to have the same size
	int square_sum = 0;
	for(int i = 0; i < size; i++) {
		square_sum += pow( arr1[i] - arr2[i], 2 );
	}
	return sqrt(square_sum);
}

int get_slope(int arr1[], int arr2[], int size) {
	int slope_sum = 0;
	for(int i = 0; i < size; i++) {
		slope_sum += abs(arr1[i] - arr2[i]);
	}
	return slope_sum / size;
}

void dft(int xn[], int len, int N) {
    float Xr[len];
    float Xi[len];
    int i, k, n;

    for (k = 0; k < N; k++) {
        Xr[k] = 0;
        Xi[k] = 0;
        for (n = 0; n < len; n++) {
            Xr[k] = (Xr[k] + xn[n] * cos(2 * M_PI * k * n / N));
            Xi[k] = (Xi[k] - xn[n] * sin(2 * M_PI * k * n / N));
        }
 
        printf("(%f) + j(%f)\n", Xr[k], Xi[k]);
    }
}

int main() {
	int arr1[] = {1, 2, 3, 4, 5};
	int arr2[] = {2, 3, 4, 5, 6};
	int dft_real[] = {1, 2, 3, 4};
	int dft_image[] = {1, 2, 3, 4};
	printf("get area %d\n",get_area(5));
	printf("get area %d\n",get_area_with_power(5));
	printf("get ball vol %d\n",get_ball_vol(5));
	printf("get ball surface %d\n",get_ball_surface(5));
	printf("get cylinder volume %d\n",get_cylind_vol(5, 10));
	printf("get cylinder surface %d\n",get_cylind_surface(5, 10));
	printf("get cone volume %d\n",get_cone_vol(5, 10));
	printf("get cone surface %d\n",get_cone_surface(5, 10));
	printf("get array average %d\n",get_arr_average(arr1, 5));
	printf("get euclidean %d\n",get_euclidean(arr1, arr2, 5));
	printf("get slope %d\n",get_slope(arr1, arr2, 5));
	dft(dft_real, 4, 4);
	return 0;
}
