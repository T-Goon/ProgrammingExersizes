java.util.Scanner;

public class Pyramid {

  public static void main(String[] args) {
    int height;
    Scanner input =  new Scanner(System.in);

    // Prompt user for height of pyramid
    System.out.print("How tall do you want to pyramid to be? ");
    height = input.nextInt();

    // Loop to make each row of pyramid
    for (int i = 0; i < height; i++){
      // Nested loop for the spacing on each row
      for (int x = height; x > i+1; x--) {
        System.out.print(" ");
      }
      // Nested loop to make the '*' on each row
      for (int y = 0; y <= i+i; y++) {
        System.out.print("*");
      }
      // New line at the end of each row
      System.out.print("\n");
    }

  }
  
}
