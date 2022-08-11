#include <stdio.h>

int sum_with_idx(int arr[], int size) {
    int sum = 0;
    for(int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}

int sum_with_while(int arr[], int size) {
    int sum = 0;
    int idx = 0;
    while (idx < size) {
        sum += arr[idx];
        idx++;
    }
    return sum;
}


int sum_with_nested(int arr[2][2], int size) {
    int sum = 0;
    for(int i = 0; i < size; ++i) {
        for(int j = 0; j < size; ++j) {
            sum += arr[i][j];
        }
    }
    return sum;
}

int sum_with_size(int size) {
    int sum = 0;
    for(int i = 0; i < size; ++i) {
        sum += i;
    }
    return sum;
}

int sum_with_sqsize(int size) {
    int sum = 0;
    for(int i = 0; i < size; ++i) {
        sum += i*i;
    }
    return sum;
}

int get_product(int arr[], int size) {
    int prod = 1;
    for(int i = 0; i < size; ++i) {
        prod *=  arr[i];
    }
    return prod;
}

int sum_of_selfprod(int *arr, int size) {
    int sum = 0;
    for(int i = 0; i < size; i++) {
        sum += arr[i]*arr[i];
    }

    return sum;
}

int sum_of_products(int* arr, int* arrx, int size) {
    int i;
    int product;
    int sum = 0;
    for(i = 0; i < size; i++) {
        product = arr[i] * arrx[i];
        sum += product;
    }

    return sum;
}

int awful_sum_of_prod(int* arr, int* arrx, int size) {
    int sum = 0;
    int sumarr[size];
    for(int i = 0; i < size; i++) {
        sumarr[i] = arr[i] * arrx[i];
        sum += sumarr[i];
    }
    return sum;
}

int main() {
    int arr[] = {5, 6, 7, 8, 9};
    int arrx[] = {1, 2, 3, 4, 5};
    int arr2[2][2] = {5, 6, 7, 8};
    printf("sum_with_idx is %d\n", sum_with_idx(arr, 5));
    printf("sum_with_while is %d\n", sum_with_while(arr, 5));
    printf("sum_with_nested is %d\n", sum_with_nested(arr2, 2));
    printf("sum_with_size is %d\n", sum_with_size(5));
    printf("sum_with_sqsize is %d\n", sum_with_sqsize(5));
    printf("get_product is %d\n", get_product(arr, 5));
    printf("sum_of_selfprod is %d\n", sum_of_selfprod(arr, 5));
    printf("sum_of_products is %d\n", sum_of_products(arr, arrx, 5));
    printf("awful_sum_of_prod is %d\n", awful_sum_of_prod(arr, arrx, 5));
    return 0;
}
