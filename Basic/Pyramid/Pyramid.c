#include <stdio.h>

int main(void) {
  int height;

  // Prompt user for height of pyramid
  printf("How tall do you want to pyramid to be? ");
  scanf("%d",&height);

  // Loop to make each row of pyramid
  for (int i = 0;i < height; i++){
    // Nested loop for the spacing on each row
    for (int x = height; x > i+1; x--) {
      printf(" ");
    }
    // Nested loop to make the '*' on each row
    for (int y = 0; y <= i+i; y++) {
      printf("*");
    }
    // New line at the end of each row
    printf("\n");
  }

  return 0;
}
