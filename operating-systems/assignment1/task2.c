#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Invalid number of arguments\n");
        exit(1);
    }

    char *word = NULL;

    for (int i = 1; i < argc; i++)
    {
        int symbol = atoi(argv[i]);

        if (symbol >= 0 && symbol <= 127)
        {
            word = (char *)realloc(word, i);

            if (word == NULL)
            {
                perror("Memory allocation failed");
                exit(1);
            }

            word[i - 1] = (char)symbol; // convert ascii int to char
        }
        else
        {
            printf("Invalid ASCII code: %s\n", argv[i]);
        }
    }

    if (word)
    {
        word[argc - 1] = '\0'; // add null terminator to end of string
        printf("%s\n", word);
        free(word);
    }

    return 0;
}
