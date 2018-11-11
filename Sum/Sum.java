import java.util.Scanner;

public class Sum {

    public static void main(String[] args) {
        int size;
        int sum = 0;
        Scanner input = new Scanner(System.in);
        
        // prompt user for size of array
        System.out.print("Enter the number of elements to be stored in the array: ");
        size = input.nextInt();
        
        // initialize array with entered size
        int array[] = new int[size];
        
        // have user fill array
        for(int i = 0;i < size;i++){
            System.out.print("Enter element "+i+": ");
            array[i] = input.nextInt();
        }
        
        // calculate the sum of all of the elements
        for(int i = 0;i < size;i++){
        sum += array[i];
        }
        
        // print out the sum
        System.out.print("The sum of all elements in the array is "+sum+".\n");
    }
    
}
