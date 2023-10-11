// Lab 3
// Name: Daim Bin Khalid
// Roll no: 251686775

// Task 4
#include <iostream>

using namespace std;

int main()
{
    int array_size, element, p;

    cout << "Enter array size: ";
    cin >> array_size;

    // declare dynamic array
    int *num_array = new int[array_size];

    cout << "Enter elements of array separated by space: ";
    for (int i = 0; i < array_size; i++)
    {
        cin >> num_array[i];
    }

    // ensure p is positive in conditional loop
    cout << "Enter positions to shift right: ";
    cin >> p;
    while (p < 0)
    {
        cout << "Enter positions to shift right: ";
        cin >> p;
    }

    // shift elements to right by moving last element to first
    // other elements moved one place to the right
    // run loop for number of right rotations
    for (int i = 0; i < p; i++)
    {
        int last_element = num_array[array_size - 1];

        // run inner loop in reverse to move last element forward
        for (int j = array_size - 1; j > 0; j--)
        {
            num_array[j] = num_array[j - 1];
        }

        // move last element to first
        num_array[0] = last_element;
    }

    cout << "Shifted Array: ";
    for (int i = 0; i < array_size; i++)
    {
        cout << num_array[i] << " ";
    }

    return 0;
}
