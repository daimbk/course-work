#ifndef MENUS_H
#define MENUS_H

#include <iostream>
#include <string>

// first menu when program starts
int baseMenu();
// menu called when user is customer
void customerMenu(std::string userType);
// menu called when user is driver
void driverMenu(std::string userType);

#endif
