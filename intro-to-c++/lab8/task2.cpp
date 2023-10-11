/* Lab 8
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 2
#include <iostream>
#include <fstream>

using std::ifstream, std::string, std::cout, std::endl;

int main()
{
    string first_name, last_name, top_name;
    int marks1, marks2, marks3, total_marks, top_marks = 0;

    // open file to read
    ifstream file("ClassList.txt");

    // reading word by word till eof
    while (file >> first_name >> last_name >> marks1 >> marks2 >> marks3)
    {
        total_marks = marks1 + marks2 + marks3;

        if (total_marks > top_marks)
        {
            top_marks = total_marks;
            top_name = first_name + " " + last_name;
        }
    }

    // print top student if exists
    if (top_name == " ")
    {
        cout << "File empty." << endl;
    }
    else
    {
        cout << top_name << " is the top student with " << top_marks << " marks." << endl;
    }

    // close file
    file.close();
    return 0;
}
