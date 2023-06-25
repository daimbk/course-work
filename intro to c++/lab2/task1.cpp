// Lab 2
// Name: Daim Bin Khalid
// Roll no.: 251686775

// Task 1
#include <iostream>
#include <cctype>

using namespace std;

int main()
{
    char letter;

    cout << "Input character: ";
    cin >> letter;
    // check if input is an alphabet
    while (!isalpha(letter))
    {
        cout << "Enter a letter only: ";
        cin >> letter;
    }
    // convert to lowercase
    letter = tolower(letter);

    switch (letter)
    {
    case 'a':
        cout << "Vowel" << endl;
        break;
    case 'e':
        cout << "Vowel" << endl;
        break;
    case 'i':
        cout << "Vowel" << endl;
        break;
    case 'o':
        cout << "Vowel" << endl;
        break;
    case 'u':
        cout << "Vowel" << endl;
        break;
    default:
        cout << "Consonant" << endl;
    }

    return 0;
}
