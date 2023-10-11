/* Lab 6
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 3
#include <iostream>

using std::cout, std::cin, std::string, std::endl;

struct StudentRecord
{
    string name;
    float test, midterm, final; // test(20%), midterm(30%), final(50%)
    char letterGrade;
};

void calGrade(StudentRecord &record)
{
    // calc percentage of total marks
    float marks = (record.test * 0.2) + (record.midterm * 0.3) + (record.final * 0.5);

    // check what letter grade student got
    if (marks >= 0 && marks < 50)
    {
        record.letterGrade = 'F';
    }
    else if (marks >= 50 && marks < 60)
    {
        record.letterGrade = 'D';
    }
    else if (marks >= 60 && marks < 75)
    {
        record.letterGrade = 'C';
    }
    else if (marks >= 75 && marks < 90)
    {
        record.letterGrade = 'B';
    }
    else if (marks >= 90 && marks <= 100)
    {
        record.letterGrade = 'A';
    }
}

void viewRecord(StudentRecord &record)
{
    cout << "\nStudent: " << record.name << endl;
    cout << "Test: " << record.test << endl;
    cout << "Midterm: " << record.midterm << endl;
    cout << "Final: " << record.final << endl;
    cout << "Grade: " << record.letterGrade << endl;
    cout << "\n";
}

int main()
{
    StudentRecord record;

    // get student info from user
    cout << "Enter student name: ";
    getline(cin, record.name);
    cout << "Test Marks: ";
    cin >> record.test;
    cout << "Midterm Marks: ";
    cin >> record.midterm;
    cout << "Final Marks: ";
    cin >> record.final;

    // call grade calculator function
    calGrade(record);
    // print results
    viewRecord(record);
}
