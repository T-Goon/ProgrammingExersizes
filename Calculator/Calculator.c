#include <stdio.h>

// Functions for calcualtor opperations
int add (int a, int b)
{
    return(a+b);
}

int sub(int a, int b)
{
    return(a-b);
}

int prod(int a, int b)
{
    return(a*b);
}

float div(int a, int b)
{
    return(a/b);
}

int rem(int a, int b)
{
    return(a%b);
}



int main()
{
    int dig1, dig2, opp, rep;
    int *p1=&dig1,*p2=&dig2,*p3=&opp;

    // Title
    printf("This is a Calculator.\n");
    
    // Loop to calculate as many times as the user wants
    do
    {
        // Prompt for 2 digits and the opperation
        printf("Enter the First Digit. Press Enter to continue.\n");
        scanf("%d",&*p1);

        printf("What operation would you like to preform?\n 1.addition\n 2.subtraction\n 3.multiplication\n 4.division\n Enter the number of the operation.(EX:1)\n");
        scanf("%d",&*p3);

        printf("Enter the second digit.\n");
        scanf("%d,",&*p2);

        // Calculate and print out the result
        switch(opp)
        {

            case 1:
                printf("%d+%d=%d\n",dig1,dig2,add(dig1,dig2));
                break;

            case 2:
                printf("%d-%d=%d\n",dig1,dig2,sub(dig1,dig2));
                break;

            case 3:
                printf("%d*%d=%d\n",dig1,dig2,prod(dig1,dig2));
                break;

            case 4:
                printf("%d/%d=%d with a remainder of %d\n",dig1,dig2,div(dig1,dig2),rem(dig1,dig2));
                break;

            default:
                printf("You have not entered a valid operation.\n");

        }
    
    // Ask if the user wants to do another calculation
    printf("Enter 1 to do another calculation or 2 to exit the program.\n");
    scanf("%d",&rep);

    }while(rep==1);

    return 0;
}
