/******************************************************************************

Lab 1
Name: Daim Bin Khalid
Roll no.: 251686775

All tasks in same file.
Task 3 done in separate file.

*******************************************************************************/
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

// Task 1
void question1()
{
    int length, width, height;
    int surface_area, volume;

    cout << "Input length, width and height separated by a single space: \n";
    cin >> length >> width >> height;

    // surface area = 2(lb + bh + lh)
    surface_area = 2 * ((length * width) + (width * height) + (length * height));

    // volume = length * width * height
    volume = length * width * height;

    cout << "Surface Area: " << surface_area << endl;
    cout << "Volume: " << volume << endl;
}

// Task 2
void question2()
{
    int number, divisor;

    cout << "Input divisor and a number to check its factor: ";
    cin >> divisor >> number;

    // check if division of the numbers produces remainder of 0 or not
    if (number % divisor == 0)
    {
        cout << divisor << " is a factor of " << number << endl;
    }
    else
    {
        cout << "Not a factor.\n\n";
    }
}

// Task 3 in separate file

// Task 4
void question4()
{
    // Celsius to Fahrenheit converter
    // formula: F = (9/5 * C) + 32

    float celsius, fahrenheit;
    cout << "Input temperature in Celsius: ";
    cin >> celsius;

    fahrenheit = 1.8 * celsius + 32;

    cout << "temperature in Fahrenheit: " << fahrenheit << " F\n\n";
}

// Task 5
void question5()
{
    // car rental bill. $30 per day + $0.5 per mile driven

    int base_rate, days;
    float total_bill, miles_driven;

    cout << "Enter days car is rented: ";
    cin >> days;
    cout << "Enter miles driven in rental car: ";
    cin >> miles_driven;

    total_bill = (30 * days) + (0.5 * miles_driven);
    cout << "Days rented cost: " << (30 * days) << "\nMiles cost: " << (0.5 * miles_driven) << endl;
    cout << "Total cost: " << total_bill << endl;
}

// Task 6
void question6()
{
    // calculating bmi from weight(kg) and height(meters) of user
    // formula: weight / height ** 2

    float weight, height;

    cout << "Enter weight in kg: ";
    cin >> weight;
    cout << "\nEnter height in meters: ";
    cin >> height;

    cout << "\nBMI: " << weight / pow(height, 2) << endl;
}

// Task 7
void question7()
{
    // convert user's age from days to years, months, days format

    int age_days, years, months, days;

    // get age in days
    cout << "Input your age in days: ";
    cin >> age_days;

    // use division and mod to get age in years months and days
    years = round(age_days / 365);
    months = age_days % 365 / 30;
    days = age_days % 365 % 30;
    cout << "Age:\nYears: " << years << "\nMonths: " << months << "\nDays: " << days;
}

int main()
{
    // calling all questions in main function

    cout << "Question 1:\n";
    question1();

    cout << "\n"
         << "Question 2:\n";
    question2();

    cout << "\n"
         << "Question 4:\n";
    question4();

    cout << "\n"
         << "Question 5:\n";
    question5();

    cout << "\n"
         << "Question 6:\n";
    question6();

    cout << "\n"
         << "Question 7:\n";
    question7();

    return 0;
}
