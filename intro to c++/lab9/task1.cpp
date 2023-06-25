/* Lab 9
Name: Daim Bin Khalid
Roll no: 251686775*/

// Task 1
#include <iostream>
#include <fstream>

using std::string;

class Vehicle
{
    string make;
    int year;
    double hp; // horse power

public:
    // setter functions
    void set_make(string in_make)
    {
        make = in_make;
    }

    void set_year(int in_year)
    {
        year = in_year;
    }

    void set_hp(double in_hp)
    {
        hp = in_hp;
    }

    // getter functions
    string get_make()
    {
        return make;
    }

    int get_year()
    {
        return year;
    }

    double get_hp()
    {
        return hp;
    }
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

    // set object values
    int counter = 0;
    while (file >> make >> year >> horsepower)
    {
        vehicles[counter].set_make(make);
        vehicles[counter].set_year(year);
        vehicles[counter].set_hp(horsepower);
        counter++;
    }

    file.close();

    return vehicles; // return pointer to array of vehicles
}

int main()
{
    int numberOfVehicles;
    Vehicle *vehicles = readVehicleInventory("vehicles", numberOfVehicles);

    // display vehicle array for checking
    for (int i = 0; i < numberOfVehicles; i++)
    {
        std::cout << vehicles[i].get_make() << " ";
        std::cout << vehicles[i].get_year() << " ";
        std::cout << vehicles[i].get_hp() << std::endl;
    }

    delete[] vehicles;

    return 0;
}
