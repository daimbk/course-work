/* Lab 7
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 2
#include <string>
#include <iostream>

using std::string, std::cout, std::endl;

class Course
{
public:
    string name;
    float test;
    float midterm;
    float final;
    char letterGrade;

    // default constructor
    Course()
    {
        name = "";
        test = 0.0;
        midterm = 0.0;
        final = 0.0;
        letterGrade = 'F';
    }

    // non-default constructor with only name argument
    Course(string name_in)
    {
        name = name_in;
        test = 0.0;
        midterm = 0.0;
        final = 0.0;
        letterGrade = 'F';
    }

    // non-default constructor with name and assessment arguments
    Course(string name_in, float test_in, float midterm_in, float final_in)
    {
        name = name_in;
        test = test_in;
        midterm = midterm_in;
        final = final_in;
        // call helper func to set grade
        calculateLetterGrade();
    }

    // getter functions
    string getName() const
    {
        return name;
    }

    float getTest() const
    {
        return test;
    }

    float getMidterm() const
    {
        return midterm;
    }

    float getFinal() const
    {
        return final;
    }

    char getLetterGrade() const
    {
        return letterGrade;
    }

    // setter functions
    void setName(string name_in)
    {
        name = name_in;
    }

    void setTest(float test_in)
    {
        test = test_in;
        // reassign letter grade with new score
        calculateLetterGrade();
    }

    void setMidterm(float midterm_in)
    {
        midterm = midterm_in;
        // reassign letter grade with new score
        calculateLetterGrade();
    }

    void setFinal(float final_in)
    {
        final = final_in;
        // reassign letter grade with new score
        calculateLetterGrade();
    }

    // display func
    void display()
    {
        cout << "Name: " << name << endl;
        cout << "Test: " << test << endl;
        cout << "Midterm: " << midterm << endl;
        cout << "Final: " << final << endl;
        cout << "Letter Grade: " << letterGrade << endl;
    }

private:
    // function to calculate letter grade
    void calculateLetterGrade()
    {
        // total = 20% of test + 30% of midterm + 50% of final
        float total = (test * 0.2) + (midterm * 0.3) + (final * 0.5);
        if (total >= 90.0)
        {
            letterGrade = 'A';
        }
        else if (total >= 75.0)
        {
            letterGrade = 'B';
        }
        else if (total >= 60.0)
        {
            letterGrade = 'C';
        }
        else if (total >= 50.0)
        {
            letterGrade = 'D';
        }
        else
        {
            letterGrade = 'F';
        }
    }
};

int main()
{
    // three Course object using all three constructors
    Course student_one;
    student_one.setName("Daim");
    student_one.setTest(90.0);
    student_one.setMidterm(85.7);
    student_one.setFinal(99.9);

    Course student_two("Ezio Auditore");
    student_two.setTest(80.0);
    student_two.setMidterm(58.9);
    student_two.setFinal(60.0);

    Course student_three("Ben 10", 60.3, 80.0, 98.5);

    // display results
    student_one.display();
    cout << "\n";
    student_two.display();
    cout << "\n";
    student_three.display();
}
