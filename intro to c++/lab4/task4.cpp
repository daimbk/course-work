/* Lab 4
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 4
#include <iostream>

using namespace std;

// func to enter score and validate
void getJudgeData(float &score)
{
    cout << "Enter score: ";
    cin >> score;

    // score range 0 - 10
    while (score < 0 || score > 10)
    {
        cout << "Incorrect. Enter score from 0-10: ";
        cin >> score;
    }
}

// get minimum score from 5 judge scores
float findLowest(float score1, float score2, float score3, float score4, float score5)
{
    float judge_scores[5] = {score1, score2, score3, score4, score5};
    float lowest = score1;

    for (int i = 1; i < 5; i++)
    {
        if (judge_scores[i] < lowest)
        {
            lowest = judge_scores[i];
        }
    }

    return lowest;
}

// get max score from 5 judge scores
float findHighest(float score1, float score2, float score3, float score4, float score5)
{
    float judge_scores[5] = {score1, score2, score3, score4, score5};
    float highest = score1;

    for (int i = 1; i < 5; i++)
    {
        if (judge_scores[i] > highest)
        {
            highest = judge_scores[i];
        }
    }

    return highest;
}

// func to calc score using average without max and min scores
void calcScore(float score1, float score2, float score3, float score4, float score5)
{
    float highest = findHighest(score1, score2, score3, score4, score5);
    float lowest = findLowest(score1, score2, score3, score4, score5);

    float judge_scores[5] = {score1, score2, score3, score4, score5};
    float total_score, average;

    for (int i = 0; i < 5; i++)
    {
        // if score is the max or min discard it
        if (judge_scores[i] != highest && judge_scores[i] != lowest)
        {
            total_score += judge_scores[i];
        }
    }

    // take average
    average = total_score / 3;
    cout << "Average score of contestant is: " << average << endl;
}

int main()
{
    // enter judge scores passed by reference to getJudgeData func
    float judge1, judge2, judge3, judge4, judge5;

    cout << "For Judge 1" << endl;
    getJudgeData(judge1);

    cout << "For Judge 2" << endl;
    getJudgeData(judge2);

    cout << "For Judge 3" << endl;
    getJudgeData(judge3);

    cout << "For Judge 4" << endl;
    getJudgeData(judge4);

    cout << "For Judge 5" << endl;
    getJudgeData(judge5);

    calcScore(judge1, judge2, judge3, judge4, judge5);

    return 0;
}
