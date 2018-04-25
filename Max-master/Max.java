import java.util.Scanner;

public class Max {

    public static void main(String[] args) {
        // variables and scanner object
        int num1, num2, num3;
        Scanner input = new Scanner(System.in);
        
        // prompt user for three numbers
        System.out.print("Enter a number: ");
        num1 = input.nextInt();
        
        System.out.print("Enter a second number: ");
        num2 = input.nextInt();
        
        System.out.print("Enter a third number: ");
        num3 = input.nextInt();
        
        // find the largest number and print it out
        if (num1 > num2 && num1 > num3){
            System.out.print(num1+"is the largest number.\n");
            System.exit(0);
        }
        else if (num2 > num3){
            System.out.print(num2+" is the largest number.\n");
            System.exit(0);
        }
        else{
            System.out.print(num3+" is the largest number.\n");
            System.exit(0);
        }
    }
    
}
