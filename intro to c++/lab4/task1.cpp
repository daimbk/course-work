/* Lab 4
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 1
#include <iostream>
#include <cstdlib>

using namespace std;

// passing score as reference
void DiceRoll(int &score)
{
    // generate random number from 1 to 6
    int roll = rand() % 6 + 1;
    cout << "Roll: " << roll << endl;
    score += roll;
}

int main()
{
    // set seed
    srand(time(0));

    int score = 0, roll_num, test;
    cout << "Enter number of times to roll dice: ";
    cin >> roll_num;

    // num of dice rolls
    for (int i = 0; i < roll_num; i++)
    {
        DiceRoll(score);
    }

    cout << "Total score after dice rolls: " << score;
    return 0;
}
