#include "menus.h"
#include "profileFunctions.h"
#include "classes.h"
#include <iostream>
#include <fstream>
#include <tuple>
#include <limits>
#include <ios>
#include <sstream>
#include <string>
#include <ctime>
#include <vector>
#include <iomanip>
#include <cmath>
#include <bits/stdc++.h>

using std::cout, std::cin, std::string, std::get, std::ifstream, std::ofstream;

// helper functions
string capitalizeEachFirstLetter(string text)
{
    for (int i = 0; i < text.length(); i++)
    {
        if (i == 0)
        {
            text[i] = toupper(text[i]);
        }
        else if (text[i - 1] == ' ')
        {
            text[i] = toupper(text[i]);
        }
    }

    return text;
}

string capitalizeFirstLetter(string text)
{
    // Convert text first letter to uppercase
    text[0] = std::toupper(text[0]);

    // Convert the remaining letters to lowercase
    for (size_t i = 1; i < text.length(); i++)
    {
        text[i] = std::tolower(text[i]);
    }

    return text;
}

// first menu when program starts
int baseMenu()
{
    std::cout << "Menu:\n\t1. Sign In\n\t2. Create Profile" << std::endl;

    int select;
    std::cout << "Enter Option: ";
    std::cin >> select;

    // range check
    while (select < 1 || select > 2)
    {
        cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // clear the input buffer
        std::cout << "Option out of range. Enter again: ";
        std::cin >> select;
    }

    return select;
}

// menu called when user is customer
void customerMenu(string userType)
{
    int select = baseMenu();

    if (select == 1)
    {
        // sign in user
        int uniqueID;
        string password;
        cout << "Enter your id: ";
        cin >> uniqueID;
        cout << "Enter your password: ";
        cin >> password;

        std::tuple credentials = signIn(userType, uniqueID, password);

        while (get<0>(credentials) == 0)
        {
            cout << "User not found. Enter valid credentials: ";
            cout << "Enter your id: ";
            cin >> uniqueID;
            cout << "Enter your password: ";
            cin >> password;
        }

        credentials = signIn(userType, uniqueID, password);
        Customer profileObj(get<0>(credentials), get<1>(credentials), get<2>(credentials), get<3>(credentials));
        profileObj.display();

        // new booking menu
        bool bookingDone = false;
        while (!bookingDone)
        {
            cout << "Profile Menu:\n\t1. Book Ride\n\t2. View Booking History\n\t3. Search Booking by Date\n\t4. Edit Profile\n\t5. Exit Menu'" << endl;
            cout << "Enter Option Number: ";
            int check;
            cin >> check;

            // check if input is within limits
            while (check < 1 || check > 5)
            {
                cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // clear the input buffer
                cout << "Option out of range. Enter again: ";
                cin >> check;
            }

            // condition executing Book Ride Option
            if (check == 1)
            {
                string paymentMethod = profileObj.setPaymentMethod();
                PaymentMethod *paymentObj = nullptr; // declare payment object for this scope
                // make PaymentMethod object according to user's choice
                if (paymentMethod == "Cash")
                {
                    paymentObj = new Cash(paymentMethod);
                }
                else
                {
                    string cardName, expDate;
                    int cardNum;

                    cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // clear the input buffer
                    cout << "Enter Card Holder Name: ";
                    getline(cin, cardName);
                    cardName = capitalizeEachFirstLetter(cardName);

                    cout << "Enter Expiration Date (MM/YY): ";
                    getline(cin, expDate);

                    cout << "Enter Card Number: ";
                    cin >> cardNum;

                    paymentObj = new CreditCard(cardName, expDate, cardNum, paymentMethod);
                }

                // take information for customer of their preferred cab booking details
                string vehicleType, pickup, destination;
                float distance;

                cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // clear the input buffer
                cout << "What type of vehicle? (Car, Van or Bike): ";
                getline(cin, vehicleType);
                // Convert vehicleType first letter to uppercase
                vehicleType = capitalizeFirstLetter(vehicleType);

                cout << "Enter pickup address: ";
                getline(cin, pickup);

                cout << "Enter destination address: ";
                getline(cin, destination);

                cout << "Enter distance (km): ";
                cin >> distance;

                // check for exact type of available driver's with customer's preferred vehicle
                ifstream driverFile("driver.txt");
                ifstream vehicleFile("vehicles.txt");

                int counter = 0, size = 5;
                int *driverList = new int[size];

                string line;
                while (getline(vehicleFile, line))
                {
                    std::stringstream ss(line);
                    string idNum, vehicle;

                    getline(ss, idNum, ',');
                    getline(ss, vehicle, ',');

                    if (vehicleType == vehicle)
                    {
                        // resize array if full
                        if (size == counter + 1)
                        {
                            size = size * 2;
                            int *tempArr = new int[size];

                            // copy elements from driverList to tempArr
                            for (int i = 0; i < counter; i++)
                            {
                                tempArr[i] = driverList[i];
                            }

                            // delete original driverList
                            delete[] driverList;

                            // assign tempArr to driverList
                            driverList = tempArr;
                        }

                        // put drivers with requested vehicle in list
                        driverList[counter] = stoi(idNum);
                        counter++;
                    }
                }

                // select a driver from list of drivers for booking
                // seed the random number generator
                std::srand(0);

                // generate a random index between 0 and size
                int index = std::rand() % counter;
                int driverID = driverList[index];

                // reopen to bring cursor to start of files
                driverFile.close();
                vehicleFile.close();

                ifstream vehicleReadFile("vehicles.txt");
                ifstream driverReadFile("driver.txt");

                // initialize vehicle attributes
                string vehicleColor, vehicleModel, vehiclePlates;

                // set vehicle attributes to create vehicle object
                while (getline(vehicleReadFile, line))
                {
                    line.erase(line.find_last_not_of("\n") + 1); // remove trailing newline character
                    std::stringstream ss(line);
                    string readID, readType, readColor, readModel, readPlates;

                    getline(ss, readID, ',');
                    getline(ss, readType, ',');
                    getline(ss, readColor, ',');
                    getline(ss, readModel, ',');
                    getline(ss, readPlates, ',');

                    if (stoi(readID) == driverID)
                    {
                        // vehicle_type is already set
                        vehicleColor = readColor;
                        vehicleModel = readModel;
                        vehiclePlates = readPlates;
                    }

                    while (getline(driverReadFile, line))
                    {
                        line.erase(line.find_last_not_of("\n") + 1); // remove trailing newline character
                        std::stringstream ss(line);
                        std::string token;
                        std::getline(ss, token, ','); // split line into tokens by comma

                        if (driverID == stoi(token))
                        {
                            // make vehicle object according to vehicle type
                            Vehicle *vehicleObj = nullptr;

                            if (vehicleType == "Car")
                            {
                                vehicleObj = new Car(vehicleType, vehicleColor, vehicleModel, vehiclePlates);
                            }
                            else if (vehicleType == "Van")
                            {
                                vehicleObj = new Van(vehicleType, vehicleColor, vehicleModel, vehiclePlates);
                            }
                            else
                            {
                                vehicleObj = new Bike(vehicleType, vehicleColor, vehicleModel, vehiclePlates);
                            }

                            getline(ss, token, ',');
                            string password = token;

                            getline(ss, token, ',');
                            string name = token;

                            getline(ss, token, ',');
                            string gender = token;

                            Driver driverObj(driverID, password, name, gender, vehicleObj);

                            // use all the created information to create booking object
                            // attributes to pass BookingInfo object: driverObj, paymentObj, pickup, destination, distance, vehicleObj
                            BookingInfo bookingObj(driverObj, paymentObj, pickup, destination, distance);

                            // loop continues till user wants to exit menu which makes flag True
                            bool exitMenu = false;
                            // cancelled flag indicates if booking would be logged or not
                            bool cancelled = false;

                            while (!exitMenu)
                            {
                                // offer option to customer to view booking or cancel it
                                cout << "Booking Menu:\n\t1. View Booking\n\t2. Cancel Booking\n\t3. Exit Menu" << endl;
                                cout << "Enter Option Number: ";
                                int option;
                                cin >> option;

                                // check if input is within limits
                                while (!(1 <= option && option <= 5))
                                {
                                    cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // clear the input buffer
                                    cout << "Option out of range. Enter again: ";
                                    cin >> option;
                                }

                                // loop will execute option then break if flag is True
                                bool back = false;
                                while (!back)
                                {
                                    if (option == 1)
                                    {
                                        cout << endl;
                                        profileObj.viewBooking(bookingObj);
                                        cout << endl;
                                        back = true;
                                    }
                                    else if (option == 2)
                                    {
                                        cout << endl;
                                        // show that booking is cancelled
                                        profileObj.cancelBooking();
                                        // returns a flag showing booking is cancelled, so it's not stored in file
                                        cancelled = true;
                                        // end parent loop
                                        exitMenu = true;
                                        break;
                                    }
                                    else
                                    {
                                        // end loop
                                        back = true;
                                        // end parent loop
                                        exitMenu = true;
                                        // end grand parent loop
                                        bookingDone = true;
                                    }
                                }
                            }

                            // store customer's booking info in their separate file to keep log
                            if (!cancelled)
                            {
                                // set current date in booking
                                std::time_t currentTime = std::time(nullptr);
                                std::tm *currentDate = std::localtime(&currentTime);
                                char date_buffer[11]; // buffer to hold the formatted date
                                std::strftime(date_buffer, sizeof(date_buffer), "%d/%m/%Y", currentDate);
                                string currentDateStr(date_buffer);

                                // open file in append mode to keep log
                                ofstream bookingFile(std::to_string(profileObj.getIdNum()) + ".txt", std::ios_base::app);
                                bookingFile << pickup << ',' << destination << ',' << distance << ',' << std::fixed << std::setprecision(2) << bookingObj.bill() << ','
                                            << driverObj.getIdNum() << ',' << driverObj.getName() << ',' << vehicleObj->getVehicleType() << ','
                                            << vehicleObj->getModel() << ',' << vehicleObj->getNumberPlate() << ',' << currentDateStr << endl;

                                bookingFile.close();

                                // update the driver's number of trips counter and their total earnings in their file
                                int previousTripCounter = 0;
                                float previousTripEarnings = 0.0;
                                // extract previous records from their file first then write after updating in list
                                // open file in read format to extract data to list
                                ifstream driverEarningsFile(std::to_string(driverObj.getIdNum()) + "earnings.txt");
                                driverEarningsFile.seekg(0);

                                while (getline(driverEarningsFile, line))
                                {
                                    line.erase(line.find_last_not_of("\n") + 1); // remove trailing newline character
                                    std::stringstream ss(line);
                                    string trips, earnings;

                                    getline(ss, trips, ',');
                                    getline(ss, earnings, ',');
                                    previousTripCounter = stoi(trips);
                                    previousTripEarnings = stof(earnings);
                                }
                                driverEarningsFile.close();

                                // update data: add 1 to trip counter and 80% of fare as driver's salary
                                previousTripCounter += 1;
                                previousTripEarnings += std::round(0.8 * bookingObj.bill() * 100) / 100.0; // rounded to 2 decimal places

                                // open file in write format to enter updated trip numbers and earnings
                                ofstream driverEarningsOutputFile(std::to_string(driverObj.getIdNum()) + ".txt");
                                driverEarningsOutputFile << std::to_string(previousTripCounter) << "," << std::to_string(previousTripEarnings) << endl;
                                driverEarningsOutputFile.close();

                                // store trip details in driver's file to keep trip record
                                ofstream driverTripFile(std::to_string(driverObj.getIdNum()) + ".txt", std::ios_base::app);
                                driverTripFile << currentDate << "," << pickup << "," << destination << "," << distance << ","
                                               << previousTripEarnings << "," << uniqueID << "," << get<2>(credentials) << "," << get<3>(credentials) << endl;

                                driverTripFile.close();
                                cout << "Booking Confirmed." << endl;
                            }

                            delete vehicleObj;
                        }
                    }

                    delete paymentObj;
                }

                delete[] driverList;
            }
            else if (check == 2)
            {
                // condition executing View Booking History option
                ifstream bookingFile(std::to_string(uniqueID) + ".txt");

                // check if file doesn't exist
                if (!bookingFile.is_open())
                {
                    cout << "\nNo trips completed yet. File does not exist.\n"
                         << endl;
                    bookingDone = true;
                }
                else
                {
                    int count = 1;
                    string line;

                    while (getline(bookingFile, line))
                    {
                        std::stringstream ss(line);
                        string pickup, destination, distance, fare, dummy, name, vehicleType, vehicleModel, plate, date;

                        getline(ss, pickup, ',');
                        getline(ss, destination, ',');
                        getline(ss, distance, ',');
                        getline(ss, fare, ',');
                        getline(ss, dummy, ',');
                        getline(ss, name, ',');
                        getline(ss, vehicleType, ',');
                        getline(ss, vehicleModel, ',');
                        getline(ss, plate, ',');
                        getline(ss, date, ',');

                        cout << "Booking " << count << ":" << endl;
                        cout << "\tDate: " << date << endl;
                        cout << "\tPickup: " << pickup << endl;
                        cout << "\tDestination: " << destination << endl;
                        cout << "\tDistance: " << distance << endl;
                        cout << "\tFare: " << fare << endl
                             << endl;
                        cout << "\tDriver Name: " << name << endl;
                        cout << "\tVehicle: " << vehicleType << " " << vehicleModel << endl;
                        cout << "\tNumber Plate: " << plate << endl
                             << endl;
                        count++;
                    }
                }

                bookingFile.close();
            }
            else if (check == 3)
            {
                // executes Search Booking by Date option
                ifstream searchFile(std::to_string(uniqueID) + ".txt");
                // check if file doesn't exist
                if (!searchFile.is_open())
                {
                    cout << "\nNo trips completed yet. File does not exist.\n"
                         << endl;
                    bookingDone = true;
                }
                else
                {
                    string searchDate;
                    cout << "Enter date to search booking (DD/MM/YYYY): ";
                    cin >> searchDate;

                    string line;
                    while (getline(searchFile, line))
                    {
                        std::stringstream ss(line);
                        string pickup, destination, distance, fare, dummy, name, vehicleType, vehicleModel, plate, date;

                        getline(ss, pickup, ',');
                        getline(ss, destination, ',');
                        getline(ss, distance, ',');
                        getline(ss, fare, ',');
                        getline(ss, dummy, ',');
                        getline(ss, name, ',');
                        getline(ss, vehicleType, ',');
                        getline(ss, vehicleModel, ',');
                        getline(ss, plate, ',');
                        getline(ss, date, ',');

                        if (date == searchDate)
                        {
                            cout << "Booking Info:" << endl;
                            cout << "\tDate: " << date << endl;
                            cout << "\tPickup: " << pickup << endl;
                            cout << "\tDestination: " << destination << endl;
                            cout << "\tDistance: " << distance << endl;
                            cout << "\tFare: " << fare << endl
                                 << endl;
                            cout << "\tDriver Name: " << name << endl;
                            cout << "\tVehicle: " << vehicleType << " " << vehicleModel << endl;
                            cout << "\tNumber Plate: " << plate << endl
                                 << endl;
                        }
                    }
                }

                searchFile.close();
            }
            else if (check == 4)
            {
                // executes Edit Profile option
                int option;

                cout << "What do you want to modify?\n\t1. Password\n\t2. Name\n\t3. Gender" << endl;
                cout << "Enter option: " << endl;
                cin >> option;

                // check if input is within limits
                while (option < 1 || option > 3)
                {
                    cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // clear the input buffer
                    cout << "Option out of range. Enter again: " << endl;
                    cin >> option;
                }

                string change;
                if (option == 1)
                {
                    cout << "Enter new password: " << endl;
                    cin >> change;
                }
                else if (option == 2)
                {
                    cout << "Enter new name: " << endl;
                    cin >> change;
                }
                else
                {
                    cout << "Enter gender: " << endl;
                    cin >> change;
                }

                editProfile(userType, uniqueID, option, change);
            }
            else
            {
                // exit main menu
                break;
            }
        }
    }
    else if (select == 2)
    {
        // credentials will have tuple of returned values having user attributes
        // the generated id from function will be passed to create_profile function
        int uniqueID = generateID();
        std::tuple<int, string, string, string> credentials = createProfile(userType, uniqueID);

        Customer profileObj(get<0>(credentials), get<1>(credentials), get<2>(credentials), get<3>(credentials));
        cout << endl;
        profileObj.display();
    }
}

// menu called when user is a driver
void driverMenu(string userType)
{
    int select = baseMenu();

    // initialize vehicleObj
    Vehicle *vehicleObj;

    if (select == 1)
    {
        // sign in user
        int uniqueID;
        string password;
        cout << "Enter your id: ";
        cin >> uniqueID;
        cout << "Enter your password: ";
        cin >> password;

        std::tuple credentials = signIn(userType, uniqueID, password);

        while (get<0>(credentials) == 0)
        {
            cout << "User not found. Enter valid credentials: ";
            cout << "Enter your id: ";
            cin >> uniqueID;
            cout << "Enter your password: ";
            cin >> password;
        }

        credentials = signIn(userType, uniqueID, password);
        Driver profileObj(get<0>(credentials), get<1>(credentials), get<2>(credentials), get<3>(credentials), vehicleObj);
        profileObj.display();

        bool exitMenu = false;
        while (!exitMenu)
        {
            int option;

            cout << "Profile Menu:\n\t1.View Total Earnings\n\t2. View Trips History\n\t3. Search Booking by Date\n\t4. Edit Profile\n\t5. Exit Menu'" << endl;
            cin >> option;

            // check if option is within limits
            while (option < 1 || option > 5)
            {
                cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // clear the input buffer
                cout << "Option out of range. Enter again: " << endl;
                cin >> option;
            }

            // setup up a nested loop to come back to Profile Menu after executing option
            bool back = false;
            while (!back)
            {
                // execute first option
                if (option == 1)
                {
                    ifstream driverEarnings(std::to_string(uniqueID) + "earnings.txt");

                    // check if file does not exist
                    if (!driverEarnings.is_open())
                    {
                        cout << "\nNo trips completed yet. File does not exist.\n";
                        back = true;
                    }
                    else
                    {
                        string line;
                        while (getline(driverEarnings, line))
                        {
                            std::stringstream ss(line);
                            string tripsCompleted, totalEarnings;

                            getline(ss, tripsCompleted, ',');
                            getline(ss, totalEarnings, ',');

                            cout << "\nTrips Completed: " << tripsCompleted << endl;
                            cout << "TotalEarning: Rs." << totalEarnings << endl;
                        }
                    }

                    driverEarnings.close();
                    back = true;
                }
                else if (option == 2)
                {
                    // execute 2nd option
                    ifstream driverTripHistory(std::to_string(uniqueID) + ".txt");

                    if (!driverTripHistory.is_open())
                    {
                        cout << "\nNo trips completed yet. File does not exist." << endl;
                        back = true;
                    }
                    else
                    {
                        int count = 1;
                        string line;
                        while (getline(driverTripHistory, line))
                        {
                            std::stringstream ss(line);
                            string date, pickup, destination, distance, fare, dummy, name, gender;

                            getline(ss, date, ',');
                            getline(ss, pickup, ',');
                            getline(ss, destination, ',');
                            getline(ss, distance, ',');
                            getline(ss, fare, ',');
                            getline(ss, dummy, ',');
                            getline(ss, name, ',');
                            getline(ss, gender, ',');

                            cout << "Booking " << count << ":" << endl;
                            cout << "\tDate: " << date << endl;
                            cout << "\tPickup: " << pickup << endl;
                            cout << "\tDestination: " << destination << endl;
                            cout << "\tDistance: " << distance << endl;
                            cout << "\tFare: " << fare << endl
                                 << endl;
                            cout << "\tCustomer Name: " << name << endl;
                            cout << "\tGender: " << gender << endl;
                            count++;
                        }
                    }

                    driverTripHistory.close();
                    back = true;
                }
                else if (option == 3)
                {
                    // executes 3rd option
                    ifstream searchTripHistory(std::to_string(uniqueID) + ".txt");

                    if (!searchTripHistory.is_open())
                    {
                        cout << "\nNo trips completed yet. File does not exist." << endl;
                        back = true;
                    }
                    else
                    {
                        string searchDate;
                        cout << "Enter date to search booking (DD/MM/YYYY): ";
                        cin >> searchDate;

                        string line;
                        while (getline(searchTripHistory, line))
                        {
                            std::stringstream ss(line);
                            string date, pickup, destination, distance, fare, dummy, name, gender;

                            getline(ss, date, ',');
                            getline(ss, pickup, ',');
                            getline(ss, destination, ',');
                            getline(ss, distance, ',');
                            getline(ss, fare, ',');
                            getline(ss, dummy, ',');
                            getline(ss, name, ',');
                            getline(ss, gender, ',');

                            if (date == searchDate)
                            {
                                cout << "Booking Info:" << endl;
                                cout << "\tDate: " << date << endl;
                                cout << "\tPickup: " << pickup << endl;
                                cout << "\tDestination: " << destination << endl;
                                cout << "\tDistance: " << distance << endl;
                                cout << "\tFare: " << fare << endl
                                     << endl;
                                cout << "\tCustomer Name: " << name << endl;
                                cout << "\tGender: " << gender << endl;
                            }
                        }
                    }

                    searchTripHistory.close();
                    back = true;
                }
                else if (option == 4)
                {
                    // executes Edit Profile option
                    int changeOption;
                    cout << "What do you want to modify?\n\t1. Password\n\t2. Name\n\t3. Gender" << endl;
                    cout << "Enter option number: ";
                    cin >> changeOption;

                    // check if input is within range
                    while (changeOption < 1 || changeOption > 3)
                    {
                        cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // clear the input buffer
                        cout << "Option out of range. Enter again: ";
                        cin >> changeOption;
                    }

                    string change;
                    if (changeOption == 1)
                    {
                        cout << "Enter new password: ";
                        cin >> change;
                    }
                    else if (changeOption == 2)
                    {
                        cout << "Enter new name: ";
                        cin >> change;
                    }
                    else
                    {
                        cout << "Enter gender: ";
                        cin >> change;
                    }

                    editProfile(userType, uniqueID, changeOption, change);
                    back = true;
                }
                else
                {
                    // flags are made True to exit loop and parent loop
                    delete vehicleObj;
                    exitMenu = true;
                    back = true;
                }
            }
        }
    }
    else if (select == 2)
    {
        // creating profile for user

        // the id will be passed to create_profile function
        int idNum = generateID();

        // take driver's vehicle info
        string vehicleType, vehicleColor, vehicleModel, vehiclePlate;
        cout << "Enter your vehicle type (Car, Van or Bike: ";
        cin >> vehicleType;
        vehicleType = capitalizeFirstLetter(vehicleType);

        cout << "Enter vehicle color: ";
        cin >> vehicleColor;
        vehicleColor = capitalizeFirstLetter(vehicleColor);

        cout << "Enter vehicle name/model: ";
        cin >> vehicleModel;
        vehicleModel = capitalizeEachFirstLetter(vehicleModel);

        cout << "Enter number plate: ";
        cin >> vehiclePlate;
        transform(vehiclePlate.begin(), vehiclePlate.end(), vehiclePlate.begin(), ::toupper);

        // store driver's vehicle info in file with their id number
        ofstream vehicleFile("vehicles.txt", std::ios_base::app);
        vehicleFile << idNum << "," << vehicleType << "," << vehicleColor << "," << vehicleModel << "," << vehiclePlate << endl;
        vehicleFile.close();

        // create vehicle object according to owner's vehicle type
        if (vehicleType == "Car")
        {
            vehicleObj = new Car(vehicleType, vehicleColor, vehicleModel, vehiclePlate);
        }
        else if (vehicleType == "Van")
        {
            vehicleObj = new Van(vehicleType, vehicleColor, vehicleModel, vehiclePlate);
        }
        else
        {
            vehicleObj = new Bike(vehicleType, vehicleColor, vehicleModel, vehiclePlate);
        }

        std::tuple<int, string, string, string> credentials = createProfile(userType, idNum);

        // make driver object with corresponding vehicle object
        Driver profileObj(get<0>(credentials), get<1>(credentials), get<2>(credentials), get<3>(credentials), vehicleObj);
        cout << endl;
        profileObj.display();

        delete vehicleObj;
    }
}
