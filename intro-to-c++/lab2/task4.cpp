// Lab 2
// Name: Daim Bin Khalid
// Roll no.: 251686775

// Task 4
#include <iostream>
#include <string>

using namespace std;

int main()
{
    int number;

    // max number for length of pyramid
    cout << "Enter positive integer only: ";
    cin >> number;
    // condition for pos int
    while (number < 1)
    {
        cout << "Enter positive integer only: ";
        cin >> number;
    }

    // upper half of pyramid
    for (int i = 0; i <= number; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            // to print multiple *
            string output(j, '*');
            cout << output << j;
        }

        cout << endl;
    }

    // lower half of pyramid
    // using reverse loop by decrement for reversing pyramid shape
    for (int i = number - 1; i >= 0; i--)
    {
        for (int j = 0; j <= i; j++)
        {
            string output(j, '*');
            cout << output << j;
        }

        cout << endl;
    }

    return 0;
}
