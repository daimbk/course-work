#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#include "validate.h"

void args_check(int argc)
{
    if (argc != 3)
    {
        printf("Usage: lab2 <filename> <number range 1 - 5>\n");
        exit(1);
    }
}

int validate_number(char *argv[])
{
    char *num = argv[2];

    // validate if last arg is an integer
    int i = 0;

    // checking for negative numbers
    if (num[0] == '-')
    {
        i = 1;
    }

    for (; num[i] != 0; i++)
    {

        if (!isdigit(num[i]))
        {
            printf("Third argument is not a number!\n");
            exit(1);
        }
    }

    int number = atoi(argv[2]);
    if (number < 1 || number > 5)
    {
        printf("Number must be between 1 and 5\n");
        exit(1);
    }

    return number;
}

void disp_file_on_console(FILE *file)
{
    char buffer[256];
    do
    {
        fgets(buffer, 256, file);

        for (int i = 0; i < strlen(buffer); i++)
        {
            printf("%c", buffer[i]);
        }

        if (feof(file))
        {
            printf("\n");
            break;
        }

    } while (1);
}

void file_decoder(FILE *file, int positions)
{
    printf("\nDecoded file:\n");

    char buffer[256];
    do
    {
        fgets(buffer, 256, file);

        for (int i = 0; i < strlen(buffer); i++)
        {
            if (buffer[i] >= 'a' && buffer[i] <= 'z')
            {
                if (buffer[i] != '\n' && buffer[i] != ',' && buffer[i] != ' ' && buffer[i] != ':' && buffer[i] != ';')
                {
                    buffer[i] = (buffer[i] - 'a' + positions) % 26 + 'a';
                }
            }

            printf("%c", buffer[i]);
        }

        if (feof(file))
        {
            printf("\n");
            break;
        }
    } while (1);
}
