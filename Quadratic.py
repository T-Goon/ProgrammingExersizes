def main():    
    print("Quadratic Equation Solver\n")
    
    # Prompt user for 'a', 'b', and 'c'
    a = float(input("Enter a: "))
    
    b = float(input("Enter b: "))
    
    c = float(input("Enter c: "))
    
    # Check if roots are imaginary or not
    if b**2-4*a*c < 0:
        print("The roots are imaginary.")
        return
        
    # Use quadratic formula to find roots
    root1 = ((b*-1)+((b**2)-4*a*c)**(.5))/(2*a)
    root2 = ((b*-1)-((b**2)-4*a*c)**(.5))/(2*a)
    
    # Print out the roots of the equation
    print("The roots of the equation are {} and {}.".format(root1, root2))
    
if __name__ == "__main__":
    main()
