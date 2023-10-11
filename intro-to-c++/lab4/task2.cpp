/* Lab 4
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 2
#include <iostream>

using namespace std;

// func to count ones in a binary conversion
void countOnes(int value)
{
    int binary_value, total_ones;

    // loop runs till value is reduced down to 0
    while (value > 0)
    {
        // get a binary value
        binary_value = value % 2;
        cout << binary_value << endl;

        // if value is 1 add to counter
        if (binary_value == 1)
        {
            total_ones += 1;
        }

        // reduce a number to check in total value
        value /= 2;
    }

    cout << "Total number of ones: " << total_ones << endl;
}

int main()
{
    int value;

    cout << "Enter a base 10 value: ";
    cin >> value;
    countOnes(value);

    return 0;
}
