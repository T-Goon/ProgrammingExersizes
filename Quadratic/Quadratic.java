import java.util.Scanner;
import java.lang.Math;

public class Quadratic {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double a,b,c;
        double root1, root2;
        
        System.out.print("Quadratic Equation Solver\n\n");
        
        // Prompt user for 'a', 'b', and 'c'
        System.out.print("Enter a: ");
        a = input.nextFloat();
        
        System.out.print("Enter b: "); 
        b = input.nextFloat();
        
        System.out.print("Enter c: ");
        c = input.nextFloat();
        
        // Check if roots are imaginary or not
        if (Math.pow(b, 2)-4*a*c < 0){
            System.out.print("The roots are imaginary.\n");
            System.exit(0);
        }
        
        // Use quadratic formula to find roots
        root1 = ((b*-1)+Math.sqrt(Math.pow(b, 2)-4*a*c))/(2*a);
        root2 = ((b*-1)-Math.sqrt(Math.pow(b, 2)-4*a*c))/(2*a);
        
        // Print out the roots of the equation
        System.out.print("The roots of the equation are "+root1+" and "+root2+".\n");
        
    }
    
}
