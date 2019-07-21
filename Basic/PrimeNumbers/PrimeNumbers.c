#include <stdio.h>

int main()
{
    int num,r;
    printf("Enter a number: ");
    scanf("%d",&num);
    for(int i=2;i<num;i++)
    {
        r=num%i;
        if(r==0)
        {
            printf("The number you have entered is not prime.\n");
            return 0;
        }
    }

    printf("The number you have entered is prime.\n");
    return 0;
}
