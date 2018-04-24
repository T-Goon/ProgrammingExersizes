#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{ 
    // Initial max number of characters and current number of characters
    unsigned int max = 128;
    unsigned int cur = 0;
 
    // malloc max amount of memory for string
    char *str = malloc(max);
    cur = max;

    // Prompt for text
    printf("Enter some text:");

    if(str != NULL)
    {
	int c = EOF;
	unsigned int i =0;
        //accept user input until hit enter or end of file
	while (( c = getchar() ) != '\n' && c != EOF)
	{
		str[i++]=(char)c;

		//if i reached maximize size then realloc size
		if(i == cur)
		{
            cur = i+max;
			str = realloc(str, cur);
		}
	}

	// Cap off string with '/0'
	str[i] = '\0';

	// Print out string backwards
	for(int i=strlen(str)-1;i>=0;i--)
    {
        printf("%c",str[i]);
    }

	// Free memory
	free(str);
	str = NULL;
    }

    return 0;
}
