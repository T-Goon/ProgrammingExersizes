public class NaturalNumbers {

    // Recursive function to print out the natural numbers from i to 50
    public static void recur(int i){
        // if i is 51 or greater stop
        if (i>50){
            return;
        }
        
        System.out.print(i+", ");
        i++;
        
        recur(i);
    }

    public static void main(String[] args) {
        
        System.out.print("The first 50 natural numbers are: ");
        
        recur(0);
        
        System.out.print("\n");
        
    }
    
}
