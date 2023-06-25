/* Lab 9
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 2
#include <iostream>
#include <fstream>

using std::string;

struct Vehicle
{
    string make;
    int year;
    double hp;
};

Vehicle *readVehicleInventory(string filepath, int &numberOfVehicles)
{
    string line;

    string make;
    int year;
    double horsepower;

    // open file for reading
    std::ifstream file(filepath + ".txt");

    // count number of lines in file = number of vehicles
    numberOfVehicles = 0;
    while (getline(file, line))
    {
        numberOfVehicles++;
    }

    file.clear();                 // clear the eof state
    file.seekg(0, std::ios::beg); // set file cursor to start of file

    // create Vehicle array
    Vehicle *vehicles = new Vehicle[numberOfVehicles];

    int counter = 0;
    while (file >> make >> year >> horsepower)
    {
        vehicles[counter].make = make;
        vehicles[counter].year = year;
        vehicles[counter].hp = horsepower;
        counter++;
    }

    file.close();

    return vehicles; // return pointer to array of vehicles
}

void mostPowerful(Vehicle *vehicles, string make, int &numberOfVehicles)
{
    double largest_hp = 0;

    // get largest hp in all object of the vehicle make
    for (int i = 0; i < numberOfVehicles; i++)
    {
        if (vehicles[i].make == make && vehicles[i].hp > largest_hp)
        {
            largest_hp = vehicles[i].hp;
        }
    }

    // print largest hp
    std::cout << "Largest horsepower of make " << make << " is " << largest_hp << std::endl;
}

int main()
{
    string make;
    int numberOfVehicles;

    Vehicle *vehicles = readVehicleInventory("vehicles", numberOfVehicles);

    std::cout << "Enter vehicle make to get largest horsepower: " << make;
    std::cin >> make;
    mostPowerful(vehicles, make, numberOfVehicles);

    delete[] vehicles;

    return 0;
}
