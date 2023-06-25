// Lab 3
// Name: Daim Bin Khalid
// Roll no: 251686775

// Task 1
#include <iostream>

using namespace std;

int main()
{
    int num_of_samples, num_of_corruptions;

    cout << "Enter number of DNA samples: ";
    cin >> num_of_samples;
    cout << "Enter number of corruptions in DNA: ";
    cin >> num_of_corruptions;

    // outer loop for each DNA sample
    for (int i = 0; i < num_of_samples; i++)
    {
        int dna_size;
        cout << "Enter size of DNA chain: ";
        cin >> dna_size;

        // declare array for DNA and counter for 'C'
        char *dna_chain = new char[dna_size];
        int counter = 0;

        // inner loop to get each DNA chain
        cout << "Enter DNA chain (each character separated by space ALL CAPS): ";
        for (int j = 0; j < dna_size; j++)
        {
            cin >> dna_chain[j];

            if (dna_chain[j] == 'C')
            {
                counter++;
            }
            else if (counter < num_of_corruptions)
            {
                counter = 0;
            }
        }

        // print result according to number of corruptions in DNA
        if (counter >= num_of_corruptions - 1)
        {
            cout << "Affected" << endl;
        }
        else
        {
            cout << "Healthy" << endl;
        }
    }

    return 0;
}
