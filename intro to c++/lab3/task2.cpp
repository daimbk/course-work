// Lab 3
// Name: Daim Bin Khalid
// Roll no: 251686775

// Task 2
#include <iostream>

using namespace std;

int main()
{
    int array_length, element, temp;

    cout << "Input length of array: ";
    cin >> array_length;

    // declare array of array_length size
    int *num_array = new int[array_length];

    // get data in array
    for (int i = 0; i < array_length; i++)
    {
        cout << "Enter an number for array: ";
        cin >> element;
        cout << endl;

        num_array[i] = element;
    }

    // print the original array
    cout << "Original Array: ";
    for (int i = 0; i < array_length; i++)
    {
        cout << num_array[i];
    }
    cout << endl;
    cout << "Size: " << array_length << endl;

    // swap first and last element
    temp = num_array[0];
    num_array[0] = num_array[array_length - 1];
    num_array[array_length - 1] = temp;

    // print the changed array
    cout << "Changed Array: ";
    for (int i = 0; i < array_length; i++)
    {
        cout << num_array[i];
    }
    cout << endl;
    cout << "Size: " << array_length << endl;

    return 0;
}
