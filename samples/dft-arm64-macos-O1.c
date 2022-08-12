#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define M 5
#define pi 3.1415926
typedef struct complex{
    double real;
    double image;
} Complex;

//struct complex fx[]={{0,7},{1,6},{2,5},{3,4},{4,3},{5,2},{6,1},{7,0}};


void init(Complex *fx);
void DFT(Complex *fu, Complex fx[]);
void IDFT(Complex fu[], Complex *fx);

int main()
{
    Complex fx[M];
    Complex fu[M];

    init(&fx[0]);

    DFT(&fu[0], fx);

    IDFT(fu, &fx);

    return 0;
}

void init(Complex *fx)
{
    int i;
    srand((int)time(0));
    for(i=0;i<M;i++){
        fx[i].real = (double)(rand()%100);
        fx[i].image = (double)(rand()%100);
        printf("f[%2d]:%8.2lf+%8.2lfj\n", i, fx[i].real, fx[i].image);
    }
    printf("-----------------------------\n");
}

void DFT(Complex *fu,Complex fx[])
{
    int u, x;
    double real,image;

    for(u=0;u<M;u++){
        real=0;
        image=0;
        for(x=0;x<M;x++){
            real+=(fx[x].real*cos(2*pi*u*x/M)-fx[x].image*(-sin(2*pi*u*x/M)));
            image+=(fx[x].image*cos(2*pi*u*x/M)+fx[x].real*(-sin(2*pi*u*x/M)));
        }
        fu[u].real=real;
        fu[u].image=image;
        printf("fu[%2d]=%8.2lf+%8.2lfj\n",u,fu[u].real,fu[u].image);
    }
}

void IDFT(Complex fu[],Complex *fx)
{
    int u,x;
    double real,image;

    for(x=0;x<M;x++){
        real=0;
        image=0;
        for(u=0;u<M;u++){
            real+=(fu[u].real*cos(2*pi*u*x/M)-fu[u].image*(sin(2*pi*u*x/M)));
            image+=(fu[u].image*cos(2*pi*u*x/M)+fu[u].real*(sin(2*pi*u*x/M)));
        }
        fx[x].real=real/M;
        fx[x].image=image/M;
        printf("fx[%2d]=%8.2lf+%8.2lfj\n",x,fx[x].real,fx[x].image);
    }
}

