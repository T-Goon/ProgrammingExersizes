#include <stdio.h>

int main()
{
    // array to be searched and variables
    int array[] = {1, 1, 3, 5, 6, 7, 9, 10};
    int target;
    int first = 0, middle, last = sizeof(array)/4;
    
    printf("Binary Search\n\n");
    
    // Prompt user for target value
    printf("What value do you want to find? ");
    scanf("%d", &target);
    
    // Calculate middle of array
    middle = (sizeof(array)/4)/2;
    
    // Loop to find the target value
    while (first<last){
        if (target > array[middle]){
            first = middle + 1;
            middle = (first + last)/2;
        }
        else{
            last = middle - 1;
            middle = (first + last)/2;
        }
        if (array[middle] == target){
            printf("The target is at index %d.\n",middle);
            return 0;
        }
    }
    
    // If the value was not found say so
    printf("The target is not in the array.\n");
    return 0;
}
