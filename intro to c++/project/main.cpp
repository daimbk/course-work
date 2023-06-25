#include "classes.h"
#include "profileFunctions.h"
#include "menus.h"

int main()
{
    std::cout << "Welcome to Daim's Cab Service" << std::endl;

    // # input if user is customer or driver
    string userType;
    std::cout << "Customer or Driver: ";
    std::cin >> userType;
    transform(userType.begin(), userType.end(), userType.begin(), ::tolower);

    // keep prompting user if input is incorrect
    while (userType != "customer" && userType != "driver")
    {
        cout << "Incorrect input. Enter Customer or Driver: ";
        cin >> userType;
        transform(userType.begin(), userType.end(), userType.begin(), ::tolower);
    }

    // call customer menu if user is customer
    if (userType == "customer")
    {
        customerMenu(userType);
    }
    else if (userType == "driver")
    {
        driverMenu(userType);
    }

    return 0;
}
