import java.util.Scanner;

public class PrimeNumbers {

    public static void main(String[] args) {
        // variable
       int num;
       
       // scanner object
       Scanner scan = new Scanner(System.in);
       
       // prompt for a number
       System.out.print("Enter a number: ");
       num = scan.nextInt();
       
       // check if the number is not prime
       for(int i=2;i<num;i++)
       {
           // if the number is not prime say so and exit the program
           if(num%i==0)
           {
               System.out.print("The number you have entered is not prime.\n");
               System.exit(0);
           }
       }
       
       // say that the number is prime and exit
       System.out.print("The number you have entered is prime.\n");
       
       System.exit(0);
      
    }
    
}
