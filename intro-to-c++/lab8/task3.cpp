/* Lab 8
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 3
#include <iostream>
#include <fstream>

using std::string, std::ifstream, std::cout, std::cin, std::endl, std::ofstream;

class Student
{
private:
    string name;
    int roll_num;
    string department;
    float gpa;

public:
    // setter functions
    void set_name(string in_name)
    {
        name = in_name;
    }

    void set_roll_num(int in_roll_num)
    {
        roll_num = in_roll_num;
    }

    void set_department(string in_department)
    {
        department = in_department;
    }

    void set_gpa(float in_gpa)
    {
        gpa = in_gpa;
    }

    // getter functions
    string get_name() const
    {
        return name;
    }

    int get_roll_num() const
    {
        return roll_num;
    }

    string get_department() const
    {
        return department;
    }

    float get_gpa() const
    {
        return gpa;
    }
};

void read_student_file(string filename, Student students[])
{
    string first_name, last_name, department;
    int roll_num;
    float gpa;

    // open file
    ifstream file(filename + ".txt");

    int counter = 0; // array counter
    // read data and store it in Student object
    while (file >> first_name >> last_name >> roll_num >> department >> gpa)
    {
        // set object values
        students[counter].set_name(first_name + " " + last_name);
        students[counter].set_roll_num(roll_num);
        students[counter].set_department(department);
        students[counter].set_gpa(gpa);
        counter++;
    }

    // close file
    file.close();
}

int main()
{
    float min_gpa;
    float average_gpa;

    // create array of students
    Student students[4];

    // call file reading function
    read_student_file("student_data", students);

    cout << "Enter minimum gpa requirement: ";
    cin >> min_gpa;
    cout << "Students with GPA greater than mentioned GPA are:" << endl;

    // display student data
    for (int i = 0; i < 4; i++)
    {
        if (students[i].get_gpa() > min_gpa)
        {
            cout << "\nName: " << students[i].get_name() << endl;
            cout << "Roll number: " << students[i].get_roll_num() << endl;
            cout << "Department: " << students[i].get_department() << endl;
            cout << "GPA: " << students[i].get_gpa() << endl;
        }

        // add all gpa for average
        average_gpa += students[i].get_gpa();
    }

    // calc average
    average_gpa /= 4;
    cout << "\nAverage GPA of all students: " << average_gpa << endl;

    // open file to write grades
    ofstream file("output.txt");

    // write student details to new file with grades
    for (int i = 0; i < 4; i++)
    {
        float gpa = students[i].get_gpa();

        file << students[i].get_name() << " ";
        file << students[i].get_roll_num() << " ";
        file << students[i].get_department() << " ";
        file << students[i].get_gpa() << " ";

        // grading conditions
        if (gpa > 3.6)
        {
            file << "A+\n";
        }
        else if (gpa > 3.3 && gpa <= 3.6)
        {
            file << "A\n";
        }
        else if (gpa > 3 && gpa <= 3.3)
        {
            file << "B\n";
        }
        else if (gpa > 2.7 && gpa <= 3)
        {
            file << "B-\n";
        }
        else if (gpa > 2.3 && gpa <= 2.7)
        {
            file << "C+\n";
        }
        else if (gpa > 2.0 && gpa <= 2.3)
        {
            file << "C\n";
        }
        else if (gpa >= 0.0 && gpa <= 2.0)
        {
            file << "F\n";
        }
    }

    file.close();
}
