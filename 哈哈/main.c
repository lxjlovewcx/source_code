#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a = 2;
    char b = 'a';
    float c = 2.5;
    unsigned int d = 2;
    short int e = 2;
    long int f = 2;
    double g = 2.5;
    printf("sizeof£¨int£© = %d\n", sizeof(a));
    printf("sizeof (char) = %d\n", sizeof(b));
    printf("sizeof (float) = %d\n", sizeof(c));
    printf("sizeof (unsigned int) = %d \n", sizeof(d));
    printf("sizeof (short int) = %d\n", sizeof(e));
    printf("sizeof (long int ) = %d\n", sizeof(f));
    printf("sizeof (double) =%d\n", sizeof(g));
    printf("a = %d\n", a);
    printf("a = %f\n", a);
    printf("a = %c\n", a);
    printf("b = %d\n", b);
    printf("b = %f\n", b);
    printf("b = %c\n", b);
    printf("c = %d\n", c);
    printf("c = %c\n", c);


    printf("c = %f\n", c);

    printf("Hello world!\n");
    return 0;
}
