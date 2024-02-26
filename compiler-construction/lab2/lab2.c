#include <stdio.h>
#include <stdlib.h>

#include "validate.h"

int main(int argc, char *argv[])
{
    args_check(argc);

    // third arg number validation
    int positions = validate_number(argv);

    FILE *file;
    file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Error opening file\n");
        exit(1);
    }

    // display file content
    disp_file_on_console(file);

    fclose(file);

    file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Error opening file\n");
        exit(1);
    }

    // decode file content
    file_decoder(file, positions);
    fclose(file);

    return 0;
}
