#include <stdio.h>

// Recursive function to print out the natural numbers from i to 50
void recur(int i){
    // if i is 51 or greater stop
    if (i > 50)
    {
        return;
    }

    printf("%d, ",i);
    i++;

    recur(i);
}

int main()
{
    printf("The first 50 natural numbers are: ");
    recur(0);
    return 0;
}
 
