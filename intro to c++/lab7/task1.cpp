/* Lab 7
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 1
#include <iostream>
#include <cmath>
#include <cstdlib>

using std::cout, std::cin, std::endl;

class Point
{
public:
    float x = 0.0;        // x coordinate
    float y = 0.0;        // y coordinate
    float distance = 0.0; // distance from origin
};

float getFurthestPoint(Point points[], int size)
{
    // func calculates distances from origin of all points in array
    // returns the index of the point with greatest distance

    float greatest_distance = points[0].distance;
    int greatest_point_index = 0;

    // get distances from origin
    for (int i = 0; i < size; i++)
    {
        points[i].distance = sqrt(pow(points[i].x, 2) + pow(points[i].y, 2));

        if (points[i].distance > greatest_distance)
        {
            greatest_distance = points[i].distance;
            greatest_point_index = i;
        }
    }

    return greatest_point_index;
};

int main()
{
    int size;

    cout << "Enter number of points: ";
    cin >> size;

    // set seed for rand
    int srand(time(0));

    // make dynamic array of size and assign coordinates
    Point points[size];
    for (int i = 0; i < size; i++)
    {
        points[i].x = rand() % (5 - (-3) + 1) + (-3);
        points[i].y = rand() % (5 - (-3) + 1) + (-3);
    }

    // call getFurthestPoint func to calculate distances of points
    int greatest_point_index = getFurthestPoint(points, size);

    // display all points
    cout << "Points:" << endl;
    for (int i = 0; i < size; i++)
    {
        cout << points[i].x << "," << points[i].y << endl;
    }

    // display greatest distance and point
    cout << "\nFurthest point and distance:\n"
         << points[greatest_point_index].x << "," << points[greatest_point_index].y << endl;
    cout << points[greatest_point_index].distance << endl;
};
