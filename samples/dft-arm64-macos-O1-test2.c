// Code from Geeksforgeeks
// https://www.geeksforgeeks.org/discrete-fourier-transform-and-its-inverse-using-c/
// C program for the above approach
#include <math.h>
#include <stdio.h>
 
// Function to calculate the DFT
void calculateDFT(int len)
{
    int xn[len];
    float Xr[len];
    float Xi[len];
    int i, k, n, N = 0;
 
    for (i = 0; i < len; i++) {
 
        printf("Enter the value "
               "of x[%d]: ",
               i);
        scanf("%d", &xn[i]);
    }
 
    printf("Enter the number of "
           "points in the DFT: ");
    scanf("%d", &N);
    for (k = 0; k < N; k++) {
        Xr[k] = 0;
        Xi[k] = 0;
        for (n = 0; n < len; n++) {
            Xr[k]
                = (Xr[k]
                   + xn[n] * cos(2 * 3.141592 * k * n / N));
            Xi[k]
                = (Xi[k]
                   - xn[n] * sin(2 * 3.141592 * k * n / N));
        }
 
        printf("(%f) + j(%f)\n", Xr[k], Xi[k]);
    }
}
 
// Driver Code
int main()
{
    int len = 0;
    printf("Enter the length of "
           "the sequence: ");
    scanf("%d4", &len);
    calculateDFT(len);
 
    return 0;
}