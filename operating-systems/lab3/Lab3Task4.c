/*
COMP 301 - B
Daim Bin Khalid
251686775
Lab 3 Task 4
*/

#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[])
{
    if (argc < 3)
    {
        printf("Not enough args");
        return 1;
    }

    char *name = argv[1];
    int age= atoi(argv[2]);

    printf("Hello %s, you are %d years old\n", name, age);

    return 0;
}
