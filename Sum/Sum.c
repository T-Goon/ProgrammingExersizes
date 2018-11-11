#include <stdio.h>

int main()
{
    int size;
    int sum = 0;

    // prompt user for size of array
    printf("Enter the number of elements to be stored in the array: ");
    scanf("%d",&size);

    // initialize array with entered size
    int array[size];

    // have user fill array
    for(int i = 0;i < size;i++){
        printf("Enter element %d: ", i);
        scanf("%d",&array[i]);
    }

    // calculate the sum of all of the elements
    for(int i = 0;i < size;i++){
        sum += array[i];
    }

    // print out the sum
    printf("The sum of all elements in the array is %d.", sum);
}
