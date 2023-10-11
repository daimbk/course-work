#ifndef PROFILEFUNCTIONS_H
#define PROFILEFUNCTIONS_H

#include <tuple>
#include <string>

using std::string;

// profile functions:
// creating new user account
// return multiple values using tuple
std::tuple<int, string, string, string> createProfile(const string &userType, const int &uniqueID);

// sign in
std::tuple<int, string, string, string> signIn(string &userType, int &uniqueID, string &password);

/* edit profile
    userType: used to open file depending on if user is customer or driver
    uniqueId: will be matched with existing data while reading profile data from file
    option: will signify what part of profile user wants to modify
    change: new changed data user will provide*/
void editProfile(string &userType, int &uniqueID, int option, string &change);

// generateID: function to generate a randomized 5 digit id number
int generateID();

#endif
