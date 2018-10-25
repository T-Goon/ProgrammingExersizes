#include <stdio.h>
#include <math.h>

int main()
{
    float a, b, c;
    float result1, result2;

    printf("Quadratic Equation Solver\n\n");

    // Prompt for 'a', 'b', and 'c'
    printf("Enter a: ");
    scanf("%f", &a);

    printf("Enter b: ");
    scanf("%f", &b);

    printf("Enter c: ");
    scanf("%f", &c);

    // Check if the roots are imaginary or not
    if (pow(b,2)-4*a*c < 0){
        printf("The roots are imaginary.");
        return 0;
    }

    // Use the quadratic formula to find roots
    result1 = ((b*-1)+sqrt(pow(b,2)-4*a*c))/(2*a);
    result2 = ((b*-1)-sqrt(pow(b,2)-4*a*c))/(2*a);

    // Print out the roots of the equation
    printf("The roots of the function are %f and %f", result1, result2);

    return 0; 
}
