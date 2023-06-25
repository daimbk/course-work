/* Lab 4
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 3
#include <iostream>

using namespace std;

int sum_of_digits(int value)
{
    int sum;

    // run loop till all numbers are added
    while (value > 0)
    {
        // get each num by mod
        sum += value % 10;
        value /= 10; // remove last number
    }

    cout << "Total: " << sum << endl;
    return sum;
}

int main()
{
    int value;

    cout << "Enter an integer value: ";
    cin >> value;
    sum_of_digits(value);

    return 0;
}
