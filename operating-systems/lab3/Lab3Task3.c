/*
COMP 301 - B
Daim Bin Khalid
251686775
Lab 3 Task 3
*/

#include <stdio.h>


void swap(int *ptr1, int *ptr2)
{
    int temp = *ptr1;
    *ptr1 = *ptr2;
    *ptr2 = temp;
}

int main()
{
    int num1 = 10, num2 = 20;

    int *ptr1, *ptr2;
    ptr1 = &num1;
    ptr2 = &num2;

    swap(ptr1, ptr2);

    printf("Num1 after swap: %d", *ptr1);
    printf("\nNum2 after swap: %d\n", *ptr2);

    return 0;
}
