/*
COMP 451 - B
Lab 1 - 19/02/2024
Daim Bin Khalid - 251686775
Syeda Manal Ammad - 251606966
*/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        perror("Invalid number of arguments!");
        printf("Usage: lab1 <file-name>\n");
        exit(1);
    }

    FILE *file;
    file = fopen(argv[1], "r");
    if (file == NULL)
    {
        perror("Error: Could not open file!");
    }

    char character;
    int char_count = 0;
    int line_count = 1;

    printf("%d. ", line_count);
    line_count++;

    do
    {
        character = fgetc(file);

        if (feof(file))
        {
            printf(" --- %d\n", char_count);
            break;
        }

        if (character == '\n')
        {
            printf(" --- %d\n%d. ", char_count, line_count);
            line_count++;
            char_count = 0;
        }
        else
        {
            printf("%c", character);
            char_count++;
        }

    } while (1);

    fclose(file);
}
