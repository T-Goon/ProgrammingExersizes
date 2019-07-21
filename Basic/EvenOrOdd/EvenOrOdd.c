#include <stdio.h>

int main(void)
{
    // prompt for a number
    printf("Enter a number ");

    int num;
    scanf("%d",&num);
    
    // check if the number is even and if it is say so, if not say it is not
    if ((num%2)==0)
    {
        printf("This number is even.\n");
    }
    else
    {
        printf("This number is odd.\n");
    }

    return 0;
}
