import java.util.Scanner;

public class Calculator {

    // Functions for calcualtor opperations
    static int add (int a, int b)
    {
        return(a+b);
    }

    static int sub(int a, int b)
    {
        return(a-b);
    }

    static int prod(int a, int b)
    {
        return(a*b);
    }

    static float div(int a, int b)
    {
        return(a/b);
    }

    static int rem(int a, int b)
    {
        return(a%b);
    }

    public static void main(String[] args) {
        int dig1, dig2, opp, rep;
        Scanner input = new Scanner(System.in);
        
        // Title
        System.out.print("This is a Calculator.\n");
        
        // Loop to calculate as many times as the user wants
        do
        {
            // Prompt for 2 digits and the opperation
            System.out.print("Enter the First Digit. Press Enter to continue.\n");
            dig1 = input.nextInt();

            System.out.print("What operation would you like to preform?\n 1.addition\n 2.subtraction\n 3.multiplication\n 4.division\n Enter the number of the operation.(EX:1)\n");
            opp = input.nextInt();

            System.out.print("Enter the second digit.\n");
            dig2 = input.nextInt();

            // Calculate and print out the result
            switch(opp)
            {

                case 1:
                    System.out.print(dig1+"+"+dig2+"="+add(dig1,dig2)+"\n");
                    break;

                case 2:
                    System.out.print(dig1+"-"+dig2+"="+sub(dig1,dig2)+"\n");
                    break;

                case 3:
                    System.out.print(dig1+"-"+dig2+"="+prod(dig1,dig2)+"\n");
                    break;

                case 4:
                    System.out.print(dig1+"/"+dig2+"="+div(dig1,dig2)+" with a remainder of "+rem(dig1,dig2)+"\n");
                    break;

                default:
                    System.out.print("You have not entered a valid operation.\n");

            }

        // Ask if the user wants to do another calculation
        System.out.print("Enter 1 to do another calculation or 2 to exit the program.\n");
        rep = input.nextInt();

    }while(rep==1);
    }
    
}
