#include "profileFunctions.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cmath>
#include <limits>
#include <ios>

using std::string, std::tuple, std::cout, std::cin, std::endl,
    std::fstream, std::ofstream, std::ifstream,
    std::ios, std::stringstream, std::to_string;

// create a new user profile
tuple<int, string, string, string> createProfile(const string &userType, const int &uniqueID)
{
    // open file in append to create if not existing
    ifstream profileFile(userType + ".txt");

    bool alreadyExists = false;
    string line;

    // check if user already exists
    while (getline(profileFile, line))
    {
        // get id from line
        stringstream ss(line);
        string idNum;
        getline(ss, idNum, ',');

        if (to_string(uniqueID) == idNum)
        {
            cout << "User with this ID already exists." << endl;
            alreadyExists = true;
            break;
        }
    }

    // close read file
    profileFile.close();

    if (!alreadyExists)
    {
        // open file to append
        ofstream writeFile(userType + ".txt", std::ios_base::app);
        string name, gender, password;

        cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // clear the input buffer
        cout << "Enter your full name: ";
        getline(cin, name);

        cout << "Gender (M/F/O): ";
        getline(cin, gender);

        cout << "Enter password: ";
        getline(cin, password);

        // write user to file
        // format: id,password,name,gender
        writeFile << uniqueID << "," << password << "," << name << "," << gender << endl;
        writeFile.close();

        return make_tuple(uniqueID, password, name, gender);
    }

    return make_tuple(0, string(), string(), string());
}

// sign in to a user account
tuple<int, string, string, string> signIn(string &userType, int &uniqueID, string &password)
{
    // open file to read
    ifstream profileFile(userType + ".txt");

    string line;
    while (getline(profileFile, line))
    {
        stringstream ss(line);
        string idNum, storedPassword, name, gender;
        getline(ss, idNum, ',');
        getline(ss, storedPassword, ',');
        getline(ss, name, ',');
        getline(ss, gender, ',');

        if (to_string(uniqueID) == idNum && password == storedPassword)
        {
            cout << endl;
            cout << "Welcome back, " << name << endl;
            profileFile.close();
            return make_tuple(stoi(idNum), storedPassword, name, gender);
        }
    }

    profileFile.close();
    return make_tuple(0, string(), string(), string());
}

// edit a user's profile
void editProfile(string &userType, int &uniqueID, int option, string &change)
{
    string fileName = userType + ".txt";
    ifstream inputFile(fileName);
    ofstream outputFile("temp.txt");

    string line;
    while (getline(inputFile, line))
    {
        stringstream ss(line);
        string idNum, password, name, gender;
        getline(ss, idNum, ',');
        getline(ss, password, ',');
        getline(ss, name, ',');
        getline(ss, gender, ',');

        if (stoi(idNum) == uniqueID)
        {
            if (option == 1)
                password = change;
            else if (option == 2)
                name = change;
            else if (option == 3)
                gender = change;
        }

        // write data to new file
        outputFile << idNum << "," << password << "," << name << "," << gender << endl;
    }

    inputFile.close();
    outputFile.close();

    // delete old file and rename accordingly
    remove(fileName.c_str());
    rename("temp.txt", fileName.c_str());

    cout << "Profile modified." << endl;
}

// generate a randomized 5-digit ID number
int generateID()
{
    srand(static_cast<unsigned>(time(nullptr)));

    int rangeStart = pow(10, 5 - 1);
    int rangeEnd = pow(10, 5) - 1;

    int newID = rand() % (rangeEnd - rangeStart + 1) + rangeStart;

    return newID;
}
