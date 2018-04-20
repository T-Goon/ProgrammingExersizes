import java.util.Scanner;

public class EvenOrOdd {

    public static void main(String[] args) {
        
        // scanner object
        Scanner scan = new Scanner(System.in);
        
        //prompt for a number
        System.out.print("Enter a number ");
        int num = scan.nextInt();
        
        //check if the number is even or odd and print out the result
        if (num % 2 ==0)
        {
            System.out.print("The number is even.\n");
        }
        else
        {
            System.out.print("The number is odd.\n");
        }
    }
    
}
