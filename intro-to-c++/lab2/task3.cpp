// Lab 2
// Name: Daim Bin Khalid
// Roll no.: 251686775

// Task 3
#include <iostream>
#include <cctype>

using namespace std;

int main()
{
    int number, zero = 0, one = 0, two = 0, three = 0, four = 0, five = 0, six = 0, seven = 0, eight = 0, nine = 0;
    int length;
    cout << "Enter numbers: ";
    cin >> number;

    length = to_string(number).length();

    for (int i = 0; i < length; i++)
    {
        switch (number % 10)
        {
        case 0:
            zero += 1;
            break;
        case 1:
            one += 1;
            break;
        case 2:
            two += 1;
            break;
        case 3:
            three += 1;
            break;
        case 4:
            four += 1;
            break;
        case 5:
            five += 1;
            break;
        case 6:
            six += 1;
            break;
        case 7:
            seven += 1;
            break;
        case 8:
            eight += 1;
            break;
        case 9:
            nine += 1;
            break;
        }

        number = number / 10;
    }

    cout << "The frequency of 0 = " << zero << endl;
    cout << "The frequency of 1 = " << one << endl;
    cout << "The frequency of 2 = " << two << endl;
    cout << "The frequency of 3 = " << three << endl;
    cout << "The frequency of 4 = " << four << endl;
    cout << "The frequency of 5 = " << five << endl;
    cout << "The frequency of 6 = " << six << endl;
    cout << "The frequency of 7 = " << seven << endl;
    cout << "The frequency of 8 = " << eight << endl;
    cout << "The frequency of 9 = " << nine << endl;

    return 0;
}
