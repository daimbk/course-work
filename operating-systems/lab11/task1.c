#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// student struct
struct Student
{
    char name[50];
    int age;
    float gpa;
};

int main()
{
    int num_students = 0;
    char continueFlag;         // y or n user input
    bool moreStudents = false; // loop flag
    int iterator = 0;          // arr iterator

    struct Student *student_array = NULL;

    do
    {
        printf("Enter data for a student? (y or n): ");
        scanf(" %c", &continueFlag);

        if (continueFlag == 'y')
        {
            moreStudents = true;

            student_array = (struct Student *)realloc(student_array, (num_students + 1) * sizeof(struct Student));

            if (student_array == NULL)
            {
                printf("Memory allocation failed\n");
                return 1;
            }

            printf("Name: ");
            scanf("%s", student_array[iterator].name);

            printf("Age: ");
            if (scanf("%d", &student_array[iterator].age) != 1)
            {
                printf("Invalid input for age. Please enter a valid integer.\n");

                // clear the input buffer to avoid an infinite loop
                int c;
                while ((c = getchar()) != '\n' && c != EOF)
                    ;

                // retry entering data for the current student
                continue;
            }

            printf("GPA: ");
            scanf("%f", &student_array[iterator].gpa);
            iterator++;
            num_students++;
        }
        else
        {
            moreStudents = false;
        }
    } while (moreStudents);

    // display data
    printf("\nStudent details:\n");
    for (int i = 0; i < num_students; ++i)
    {
        printf("Student %d:\n", i + 1);
        printf("Name: %s\n", student_array[i].name);
        printf("Age: %d\n", student_array[i].age);
        printf("GPA: %.2f\n", student_array[i].gpa);
        printf("\n");
    }

    free(student_array);

    return 0;
}
