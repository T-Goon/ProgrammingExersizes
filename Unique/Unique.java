import java.util.Scanner;

public class Unique {

    public static void main(String[] args) {
        int size;
        Scanner input = new Scanner(System.in);
        
        // Prompt user for size of array
        System.out.print("Enter the number of elements to be stored in the array: ");
        size = input.nextInt();
        
        // initialize array
        int array[] = new int[size];
        
        // Have user fill the array
        for(int i=0;i<size;i++){
            System.out.print("Enter element "+i+": ");
            array[i] = input.nextInt();
        }
        
        // array to hold the unique elements
        int unique[] = new int[size];
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
        System.out.print("The unique elements of the array are: ");
        for(int i=0;i<index;i++){
            System.out.print(unique[i]+", ");
        }
        
    }
    
}
