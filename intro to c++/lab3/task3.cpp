// Lab 3
// Name: Daim Bin Khalid
// Roll no: 251686775

// Task 3
#include <iostream>
#include <cctype>

using namespace std;

int main()
{
    string string_input;

    // get an input with spaces
    cout << "Input a string: ";
    getline(cin, string_input);

    // loop through the string to get each letter
    // if conditions for all requirements
    for (int i = 0; i < string_input.length(); i++)
    {
        if (islower(string_input[i]))
        {
            cout << "Character " << string_input[i] << " at index " << i << " is lowercase" << endl;
        }
        else if (isupper(string_input[i]))
        {
            cout << "Character " << string_input[i] << " at index " << i << " is uppercase" << endl;
        }
        else if (string_input[i] == ' ')
        {
            cout << "Character at index " << i << " is a space" << endl;
        }
        else if (isalpha(string_input[i]))
        {
            cout << "Character " << string_input[i] << " at index " << i << " is not an alphabet or space" << endl;

            return 0;
        }
    }
}
