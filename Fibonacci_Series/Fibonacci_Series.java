import java.util.Scanner;

public class Fibonacci_Series {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // Variables and Title
        int a = 1, b = 1, num;
        Scanner input = new Scanner(System.in);
        
        System.out.print("Fibonacci Series\n\n");
        
        // Prompt user for input
        System.out.print("How many numbers of the Fibonacci Series do you want to print? ");
        num = input.nextInt();
        
        // if the input is 1 or 2 print it out and then exit
         if (num == 1)
        {
            System.out.print(a);
            System.exit(0);
        }else if (num == 2)
        {
            System.out.print(a+", "+b);
            System.exit(0);
        }
         
        // print out the first 2 in series when input is more than 2 and recalculate 'a' and 'b'
        System.out.print(a+", "+b+", ");
        a=b+a;
        b=a+b;
        
        // counter variable
        int i=0;

        // loop to print out the series for any amount beyond 2
         while (i<num-2)
        {
            System.out.print(a+", ");
            i++;

            if(i==num-2)
                {break;}

            System.out.print(b+", ");
            i++;

            a=b+a;
            b=a+b;
        }

        System.exit(0);
    }
    
}
