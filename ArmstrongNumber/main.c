#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num,rem,sum=0,check;
    printf("Enter a number.\n");
    scanf("%d",&num);
check=num;
while(num!=0)
{
    rem=num%10;
    num/=10;
    sum+=(rem*rem*rem);
}
if(sum==check)
{
    printf("The number you entered is an armstrong number.");

}else printf("The number you entered is not an armstrong number.");
    return 0;
}

