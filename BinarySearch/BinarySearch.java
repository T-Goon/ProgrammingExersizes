import java.util.Scanner;

public class BinarySearch {

    public static void main(String[] args) {
        // array to be searched and variables
        int array[] = {1, 1, 3, 5, 6, 7, 9, 10};
        int target;
        int first = 0, middle, last = array.length;
        Scanner input = new Scanner(System.in);
        
        System.out.print("Binary Search\n\n");
        
        // Prompt user for target value
        System.out.print("What value do you want to find? ");
        target = input.nextInt();
        
        // Calculate the middle of the array
        middle = array.length / 2;
        
        // Loop to find the target value
        while (first <= last){
            if (array[middle] == target){
                System.out.print("The target is at index "+middle+".\n");
                System.exit(0);
            }
            else if (target > array[middle]){
                first = middle + 1;
                middle = (first + last)/2;
            }
            else{
                last = middle - 1;
                middle = (first + last)/2;
            }
        }
        
        System.out.print("The target is not in the array.\n");
        System.exit(0);
    }
    
}
