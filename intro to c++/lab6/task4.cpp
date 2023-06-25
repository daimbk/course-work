/* Lab 6
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 4
#include <iostream>

using std::cin, std::cout, std::string;

struct Drink
{
    string name;
    double cost;
    int quantity;
};

void displayMenu(Drink drinks[], int size)
{
    cout << "\nWelcome to the soft drink machine!\n";
    cout << "------------------------------\n";
    for (int i = 0; i < size; i++)
    {
        cout << i + 1 << ". " << drinks[i].name << " ($" << drinks[i].cost << ")\n";
    }
    cout << size + 1 << ". Quit\n";
}

void buyDrink(Drink &drink)
{
    // func to buy drink, includes cost validation checks
    double money;
    cout << "Please insert $" << drink.cost << ": ";
    cin >> money;

    // range check from 0 to 1 dollars
    if (money < 0 || money > 1.0)
    {
        cout << "Invalid amount. Please try again.\n";
        return;
    }

    double change = money - drink.cost;
    if (change < 0)
    {
        cout << "Not enough money. Please insert more.\n";
        return;
    }

    drink.quantity--;
    // message to show successful dispensing
    cout << "Dispensing " << drink.name << "...\n";
    if (change > 0)
    {
        cout << "Your change is $" << change << ".\n";
    }
}

int main()
{
    // declare object array of 4 items
    const int size = 4;
    Drink drinks[size] = {
        {"Cola", 0.75, 20},
        {"Root Beer", 0.75, 20},
        {"Grape Soda", 0.80, 20},
        {"Cream Soda", 0.80, 20}};

    // store total earnings
    double totalEarnings = 0;
    bool quit = false; // flag to quit when user selects to
    while (!quit)
    {
        displayMenu(drinks, size);

        int choice;
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice < 1 || choice > size + 1)
        {
            cout << "Invalid choice. Please try again.\n";
        }
        else if (choice == size + 1)
        {
            quit = true;
        }
        else if (drinks[choice - 1].quantity == 0)
        {
            cout << "Sorry, " << drinks[choice - 1].name << " is sold out.\n";
        }
        else
        {
            buyDrink(drinks[choice - 1]);
            totalEarnings += drinks[choice - 1].cost;
        }
    }

    cout << "\nThank you for using the soft drink machine!\n";
    cout << "Total earnings: $" << totalEarnings << "\n";

    return 0;
}
