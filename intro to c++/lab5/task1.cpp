/* Lab 5
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 1
#include <iostream>

using namespace std;

int main()
{
    int first_value = 5, second_value = 15;
    int *p1, *p2;

    p1 = &first_value;  // p1 = address of first_value
    p2 = &second_value; // p2 = address of second_value

    *p1 = 10;  // value pointed by p1 = 10
    *p2 = *p1; // value pointed by p2 = value pointed by p1
    p1 = p2;   // p1 = p2(address of pointer is copied)
    *p1 = 20;  // value pointed by p1 = 20

    // print first_value and second_value
    cout << first_value << "\n"
         << second_value << "\n";

    return 0;
}
