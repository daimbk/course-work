/*
COMP 301 - B
Daim Bin Khalid
251686775
Lab 3 Task 2
*/

#include <stdio.h>


int main()
{
    int int_arr[5] = {0, 1, 2, 3, 4};

    int *arr_ptr;
    
    for (int i = 0; i < 5; i++) {
        arr_ptr = &int_arr[i];
        printf("%d\n", *arr_ptr);
    }

    return 0;
}
