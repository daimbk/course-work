/******************************************************************************

Lab 1
Name: Daim Bin Khalid
Roll no.: 251686775

*******************************************************************************/
#include <iostream>
#include <string>

using namespace std;

// Task 3
// find number of characters in an input string
int main()
{
    string sentence;
    int length;

    cout << "Input sentence to get its number of characters: \n";
    // use getline to read string with spaces
    getline(cin, sentence);

    // string_name.length() function produces number of characters
    cout << "Length is: " << sentence.length() << endl;

    return 0;
}
