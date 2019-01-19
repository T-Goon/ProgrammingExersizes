#include <stdio.h>
#include <process.h>

int main(void) {
  char background[100];
  char text[100];
  printf("CMD Color Changer\n\n");
  printf("0 = black\n1 = blue\n2 = green\n3 = Aqua\n4 = Red\n"
  "5 = Purple\n6 = Yellow\n7 = Light Grey\n8 = Grey\n"
  "9 = Light Blue\nA = Light Green\nB = Light Green\n"
  "C = Light Red\nD = Light Purple\nE = Light Yellow\n"
  "F = White\n");

  printf("Choose a background color: ");
  scanf("%s", &background);

  printf("Choose a text color: ");
  scanf("%s", &text);

  spawnl(P_WAIT, "color_changer.cmd", "color_changer.cmd",
  background, text, NULL);

  return 0;
}
