import java.util.Scanner;

public class Reverse {

    public static void main(String[] args) {
        String txt;
        Scanner input = new Scanner(System.in);
        
        // prompt user for text
        System.out.print("Enter some text: ");
        txt = input.nextLine();
        
        // print out string backwards
        for(int i=txt.length()-1;i>=0;i--)
        {
            System.out.print(txt.charAt(i));
        }
    }
    
}
