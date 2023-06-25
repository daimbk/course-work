/* Lab 5
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 2
#include <iostream>

// passing array pointer and size
void swapAcrossCenter(int *arr, int size)
{
    // get center index
    int center = size / 2;

    int temp;
    for (int i = 0; i < center; i++)
    {
        // calculate corresponding index on the other side of center
        int opposite_index = size - i - 1;

        // swap elements
        temp = arr[i];
        arr[i] = arr[opposite_index];
        arr[opposite_index] = temp;
    }
}

int main()
{
    // odd number of elements
    int num_array[] = {1, 2, 3, 4, 5};

    swapAcrossCenter(num_array, 5);
    for (int i = 0; i < 5; i++)
    {
        // display elements
        std::cout << num_array[i] << std::endl;
    }
}
