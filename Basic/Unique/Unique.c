#include <stdio.h>

int main()
{
    int size;

    // Prompt user for size of array
    printf("Enter the number of elements to be stored in the array: ");
    scanf("%d",&size);

    // initialize array
    int array[size];

    // Have user fill the array
    for(int i=0;i<size;i++){
        printf("Enter element %d: ",i);
        scanf("%d",&array[i]);
    }

    // array to hold the unique elements
    int unique[size];
    int index = 0;

    // Check if each element in the array is unique and if it is add it to the unique array
    for (int i=0;i<size;i++){
        // Count how many of each number is in the array
        int count = 0;
        for(int j=0;j<size;j++){
            if(array[i] == array[j])
                count++;
        }
        // If there is only one in the array add that number to the "unique" array
        if(count == 1){
            unique[index] = array[i];
            index++;
        }
    }

    // Print out the unique elements of the array
    printf("The unique elements in the array are: ");
    for(int i=0;i<index;i++){
        printf("%d, ",unique[i]);
    }

    return 0;
}
