#include <stdio.h>

int main()
{
    int num1, num2, num3;

    // prompt user for three numbers
    printf("Enter a number: ");
    scanf("%d",&num1);

    printf("Enter a second number: ");
    scanf("%d",&num2);

    printf("Enter a third number: ");
    scanf("%d",&num3);

    // find which number is the greatest and return
    if (num1 > num2 && num1 > num3){
        printf("%d is the greatest number.", num1);
        return 0;
    }
    else if (num2 > num3){
        printf("%d is the greatest number.", num2);
        return 0;
    }
    else{
        printf("%d is the greatest number.", num3);
        return 0;
    }

}
