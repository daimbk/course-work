#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc < 3) {
        printf("Invalid arguments");
        exit(1);
    }

    char *name = argv[1];
    int roll_num = atoi(argv[2]);

    FILE *fptr = fopen("students.txt", "a");

    while (roll_num != -1) {
        fprintf(fptr, "%s\t%d\n", name, roll_num);

        printf("Enter new student name: ");
        scanf("%s", *&name);

        printf("Enter roll number: ");
        scanf("%d", &roll_num);
    }

    fclose(fptr);

    FILE *read_file;

    if ((read_file = fopen("students.txt", "r")) == NULL) {
        printf("Error opening file for reading");
        exit(1);
    };

    int status;

    while (status != -1)
    {
        status = fscanf(read_file, "%s\t%d", name, &roll_num);
        printf("Student: %s, Roll Number: %d\n", name, roll_num);
    } 

    fclose(read_file);

    return 0;
}
