#include <stdio.h>

int main()
{
    // Variables and Title
    int a = 1, b = 1, num;

    printf("Fibonacci Series\n\n");

    // Prompt user for input
    printf("How many numbers of the Fibonacci Series do you want to print? ");
    scanf("%d",&num);

    // if the input is 1 or 2 print it out and then exit
    if (num == 1)
    {
        printf("%d",a);
        return 0;
    }else if (num == 2)
    {
        printf("%d, %d",a,b);
        return 0;
    }

    // print out the first 2 in series when input is more than 2 and recalculate 'a' and 'b'
    printf("%d, %d, ",a,b);
    a=b+a;
    b=a+b;

    // counter variable
    int i=0;

    // loop to print out the series for any amount beyond 2
    while (i<num-2)
    {
        printf("%d, ",a);
        i++;

        if(i==num-2)
            {break;}

        printf("%d, ",b);
        i++;

        a=b+a;
        b=a+b;
    }

    return 0;
}
