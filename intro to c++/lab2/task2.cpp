// Lab 2
// Name: Daim Bin Khalid
// Roll no.: 251686775

// Task 2
#include <iostream>

using namespace std;

int main()
{
    // three levels of nested loop to get combinations
    // run loop till 100 as per required condition
    for (int i = 1; i <= 100; i++)
    {
        for (int j = 1; j <= 100; j++)
        {
            for (int k = 1; k <= 100; k++)
            {
                // the if condition checks task requirements
                if ((i + j + k <= 100) && (i * i + j * j == k * k))
                {
                    cout << "Side 1: " << i << " Side 2: " << j << " Hypotenuse: " << k << endl;
                }
            }
        }
    }

    return 0;
}
