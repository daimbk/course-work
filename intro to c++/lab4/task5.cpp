/* Lab 4
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 5
// used fix number of students = 5
#include <iostream>
#include <limits>

using namespace std;

// func to enter names and test scores
void student_data(string (&names)[5], int (&scores)[5][5])
{
    // outer loop gets names
    for (int i = 0; i < 5; i++)
    {
        cout << "Enter name of student: ";
        getline(cin, names[i]);

        // inner loop gets test scores for each student
        for (int j = 0; j < 5; j++)
        {
            cout << "Enter score for test " << j + 1 << ": ";
            cin >> scores[i][j];

            // range check
            while (scores[i][j] < 0 || scores[i][j] > 100)
            {
                cout << "Out of range. Enter again: ";
                cin >> scores[i][j];
            }
        }

        // clear the input buffer to avoid problems with future input
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << endl;
    }
}

// func to calculate avg score
void calcGrade(string (&names)[5], int (&scores)[5][5], float (&grades)[5])
{
    int total_score;
    float average;

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            total_score += scores[i][j];
        }

        // get avg and push to array
        average = total_score / 5;
        grades[i] = average;

        // reset for next cycle
        total_score = 0;
        average = 0;
    }
}

// display func
void display_result(string (&names)[5], int (&scores)[5][5], float (&grades)[5])
{
    cout << "Results:" << endl;

    for (int i = 0; i < 5; i++)
    {
        cout << "Name of student: " << names[i] << endl;

        for (int j = 0; j < 5; j++)
        {
            cout << "Score for test " << j + 1 << ": " << scores[i][j] << endl;
        }

        // print grade according to average test score
        if (grades[i] > 90)
        {
            cout << "Average: " << grades[i] << endl;
            cout << "Grade: A\n";
        }
        else if (grades[i] > 80)
        {
            cout << "Average: " << grades[i] << endl;
            cout << "Grade: B\n";
        }
        else if (grades[i] > 70)
        {
            cout << "Average: " << grades[i] << endl;
            cout << "Grade: C\n";
        }
        else if (grades[i] > 60)
        {
            cout << "Average: " << grades[i] << endl;
            cout << "Grade: D\n";
        }
        else
        {
            cout << "Average: " << grades[i] << endl;
            cout << "Grade: F\n";
        }

        cout << endl;
    }
}

int main()
{
    // pass arrays by reference to all functions
    string names[5];
    int scores[5][5];
    float grades[5];

    student_data(names, scores);
    calcGrade(names, scores, grades);
    display_result(names, scores, grades);

    // calc and display class average
    float class_grade;
    for (int i = 0; i < 5; i++)
    {
        class_grade += grades[i];
    }

    cout << "Class Average: " << class_grade / 5;

    return 0;
}
