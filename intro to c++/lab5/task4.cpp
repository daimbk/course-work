/* Lab 5
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 4
#include <iostream>

using namespace std;

void Input(int **&matrix, int size)
{
    // get memory for matrix
    matrix = new int *[size];
    for (int i = 0; i < size; i++)
    {
        // initialize a column array at each row index
        matrix[i] = new int[size];
    }

    // get input from user for each row and column
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            cout << "Enter data for row " << i + 1 << " column " << j + 1 << ": ";
            cin >> matrix[i][j];
        }
    }
}

void Display(int **matrix, int size)
{
    // display arrays in matrix format
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            cout << matrix[i][j] << " ";
        }

        cout << endl;
    }
}

void ReverseDiagonal(int **matrix, int size)
{
    // reverse first diagonal using temp variable
    for (int i = 0; i < size - 1; i++)
    {
        for (int j = i + 1; j < size; j++)
        {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }

    // reverse second diagonal
    for (int i = 0, j = size - 1; i < size / 2; i++, j--)
    {
        int temp = matrix[i][i];
        matrix[i][i] = matrix[j][j];
        matrix[j][j] = temp;

        temp = matrix[i][j];
        matrix[i][j] = matrix[j][i];
        matrix[j][i] = temp;
    }
}

int main()
{
    int **matrix;
    int size;

    // get size from user
    do
    {
        cout << "Enter size of square matrix: ";
        cin >> size;

    } while (size <= 0);

    // get input from user
    Input(matrix, size);

    // display matrix
    cout << "Original matrix:" << endl;
    Display(matrix, size);

    // reverse diagonals
    ReverseDiagonal(matrix, size);

    // display matrix with reversed diagonals
    cout << "Matrix with reversed diagonals:" << endl;
    Display(matrix, size);

    // delete each pointer/matrix array to free memory
    for (int i = 0; i < size; i++)
    {
        delete[] matrix[i];
    }

    delete[] matrix;

    return 0;
}
