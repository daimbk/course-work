// Daim Bin Khalid
// 251686775
// 24/03/2024

#include <stdio.h>
#include <stdlib.h>

#include "helper.h"

// preprocessor functions
void removeBlankLines(char *inputFile, char *outputFile);
void removeComments(char *inputFile, char *outputFile);
void macroExpansion(char *inputFile, char *outputFile);

int main(int argc, char **argv)
{
    if (argc != 5)
    {
        printf("Usage: %s <inputFile> <noBlanksFile> <noCommentsFile> <macroExpansionFile>\n", argv[0]);
        return 1;
    }

    removeBlankLines(argv[1], argv[2]);
    removeComments(argv[2], argv[3]);
    macroExpansion(argv[3], argv[4]);

    return 0;
}

void removeBlankLines(char *inputFile, char *outputFile)
{
    FILE *readFile = fopen(inputFile, "r");
    if (readFile == NULL)
    {
        printf("Couldn't open %s\n", inputFile);
        exit(1);
    }

    FILE *blankFile = fopen(outputFile, "w");
    if (blankFile == NULL)
    {
        printf("Couldn't open %s\n", outputFile);
        exit(1);
    }

    char buffer[256];
    while (fgets(buffer, sizeof(buffer), readFile) != NULL)
    {
        if (buffer[0] != '\n')
        {
            fprintf(blankFile, "%s", buffer);
        }
    }

    fclose(readFile);
    fclose(blankFile);
}

void removeComments(char *inputFile, char *outputFile)
{
    FILE *readFile = fopen(inputFile, "r");
    if (readFile == NULL)
    {
        printf("Couldn't open %s\n", inputFile);
        exit(1);
    }

    FILE *noCommentFile = fopen(outputFile, "w");
    if (noCommentFile == NULL)
    {
        printf("Couldn't open %s\n", outputFile);
        exit(1);
    }

    char buffer[256];
    int blockComment = 0;

    while (fgets(buffer, sizeof(buffer), readFile) != NULL)
    {
        for (int i = 0; buffer[i] != '\0'; i++)
        {
            // check for single line comments
            if (buffer[i] == '/' && buffer[i + 1] == '/')
            {
                break;
            }

            // check for start of block comment
            if (!blockComment && buffer[i] == '/' && buffer[i + 1] == '*')
            {
                blockComment = 1;
                i++;
            }

            // check for end of block comment
            else if (blockComment && buffer[i] == '*' && buffer[i + 1] == '/')
            {
                blockComment = 0;
                i+=2;
            }

            // write to file if not comment
            else if (!blockComment)
            {
                fputc(buffer[i], noCommentFile);
            }
        }
    }

    fclose(readFile);
    fclose(noCommentFile);
}

// struct to hold macro name and value pairs
struct Macro {
    char name[256];
    char value[256];
};

void macroExpansion(char *inputFile, char *outputFile) {
    FILE *readFile = fopen(inputFile, "r");
    if (readFile == NULL) {
        printf("Couldn't open %s\n", inputFile);
        exit(1);
    }

    FILE *macrosFile = fopen(outputFile, "w");
    if (macrosFile == NULL) {
        printf("Couldn't open %s\n", outputFile);
        exit(1);
    }

    char buffer[256];
    struct Macro macros[100];
    int numOfMacros = 0;

    while (fgets(buffer, sizeof(buffer), readFile) != NULL) {
        if (buffer[0] == '#' && buffer[1] == 'd') {
            // extract macro name and value
            char macroName[256], macroValue[256];
            stringScanf(buffer, "#define %s %[^\n]", macroName, macroValue);

            // store macro in macros array
            copyString(macros[numOfMacros].name, macroName);
            copyString(macros[numOfMacros].value, macroValue);
            numOfMacros++;
        } else {
            // macro replacement in the line
            int i = 0;
            while (buffer[i] != '\0') {
                int foundMacro = -1;
                // check if current position matches any macro
                for (int j = 0; j < numOfMacros; j++) {
                    int k = 0;

                    // check for complete match of macro name
                    while (macros[j].name[k] != '\0' && buffer[i + k] == macros[j].name[k]) {
                        k++;
                    }

                    if (macros[j].name[k] == '\0') {
                        foundMacro = j;
                        break;
                    }
                }

                // macro found, replace it with its value
                if (foundMacro != -1) {
                    fputs(macros[foundMacro].value, macrosFile);
                    i += stringLength(macros[foundMacro].name); // move index to after the macro name
                } else {
                    // write character as is if no match
                    fputc(buffer[i], macrosFile);
                    i++;
                }
            }
        }
    }

    fclose(readFile);
    fclose(macrosFile);
}
