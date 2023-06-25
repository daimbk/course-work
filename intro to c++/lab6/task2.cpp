/* Lab 6
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 2
#include <iostream>

using std::cout, std::cin, std::string, std::endl;

struct StringStat
{
    string s;
    int lower = 0, upper = 0, digit = 0;
};

int main()
{
    // create array of 5 objects
    StringStat stat_arr[5];

    // get input for each 5 string from user
    for (int i = 0; i < 5; i++)
    {
        cout << "Input a string: ";
        cin >> stat_arr[i].s;
    }

    // count uppercase, lowercase and digits in each string
    for (int i = 0; i < 5; i++)
    {
        // loop using each character in string
        for (char c : stat_arr[i].s)
        {
            // if char is uppercase increment
            if (isupper(c))
            {
                stat_arr[i].upper++;
            }

            // if char is lowercase increment
            if (islower(c))
            {
                stat_arr[i].lower++;
            }

            // if char is digit increment
            if (isdigit(c))
            {
                stat_arr[i].digit++;
            }
        }
    }

    // print all stats
    for (int i = 0; i < 5; i++)
    {
        cout << "\nString: " << stat_arr[i].s << endl;
        cout << "Lowercase Characters: " << stat_arr[i].lower << endl;
        cout << "Uppercase Characters: " << stat_arr[i].upper << endl;
        cout << "Digit Characters: " << stat_arr[i].digit << endl;
        cout << "\n";
    }
}
