/* Lab 5
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 3
#include <iostream>

using namespace std;

int *DoubleIt(int *arr, int &size)
{
    // declare new array with double the inserted size
    int *new_array = new int[2 * size];

    // second half index starting point
    int second_half = size;

    // add value 0 to first half and previous array to second half
    for (int i = 0; i < size; i++)
    {
        new_array[i] = 0;
        new_array[second_half] = arr[i];
        second_half++;
    }

    // return pointer to new array
    return new_array;
}

int main()
{
    int *arr;
    int size;

    cout << "Enter array size: ";
    cin >> size;
    // make dynamic array
    arr = new int[size];

    // get array data from user
    for (int i = 0; i < size; i++)
    {
        cout << "Enter data for array: ";
        cin >> arr[i];
    }

    // get pointer to new array
    int *new_array = DoubleIt(arr, size);

    // print new array
    for (int i = 0; i < size * 2; i++)
    {
        cout << new_array[i] << "\n";
    }

    // free the used memory
    delete[] arr;
    delete[] new_array;

    return 0;
}
