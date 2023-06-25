/* Lab 8
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 1
#include <iostream>
#include <fstream>

using std::cout, std::cin, std::ofstream;

int main()
{
    int n;

    cout << "Enter a positive integer: ";
    cin >> n;

    // open file
    ofstream file("multiplicationTable.txt");

    // nested loop multiplies and creates n tables till n^2
    for (int i = 1; i <= n; ++i)
    {
        for (int j = 1; j <= n; ++j)
        {
            int result = i * j;

            // write result to file
            file << result << " ";
        }

        file << '\n';
    }

    // close file
    file.close();
    return 0;
}
