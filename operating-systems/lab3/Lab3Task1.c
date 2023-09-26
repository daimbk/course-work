/*
COMP 301 - B
Daim Bin Khalid
251686775
Lab 3 Task 1
*/

#include <stdio.h>


int main()
{
    int num = 10;
    int *ptr_num;
    ptr_num = &num;

    printf("Num values: %d\n", num);
    printf("Pointer value: %d\n", *ptr_num);

    return 0;
}
