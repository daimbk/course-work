/* Lab 6
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 1
#include <iostream>

using std::cout, std::cin;

struct RationalNumber
{
    int a; // numerator
    int b; // denominator
};

double toDouble(RationalNumber &r_num)
{
    // converts rational number to double

    // convert numerator to double to avoid logical error
    double result = (double)r_num.a / r_num.b;
    return result;
}

int main()
{
    // declare a RationalNumber object
    RationalNumber rational_num;

    // get numerator and denominator from user
    cout << "Enter numerator: ";
    cin >> rational_num.a;

    cout << "Enter denominator: ";
    cin >> rational_num.b;

    // toDouble func call
    double result_double = toDouble(rational_num);

    // print result
    cout << "Answer in double is: " << result_double;

    return 0;
}
