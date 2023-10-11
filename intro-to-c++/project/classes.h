#ifndef CLASSES_H
#define CLASSES_H

#include <string>
#include <iostream>
#include <cctype>
#include <algorithm>

using std::string, std::cin, std::cout, std::endl;

// forward declarations
class BookingInfo;

// abstract class for various vehicle types
class Vehicle
{
protected:
    string vehicleType;
    string color;
    string model;
    string numberPlate;

public:
    Vehicle(const string &vehicleType, const string &color, const string &model, const string &numberPlate);

    // getter functions
    string getVehicleType() const;
    string getColor() const;
    string getModel() const;
    string getNumberPlate() const;

    void display() const;
};

// abstract class for user type
class Profile
{
protected:
    int id_num;
    string password;
    string name;
    string gender;

public:
    Profile(const int &id_num, const string &password, const string &name, const string &gender);

    // getter functions
    string getName() const;
    int getIdNum() const;
    string getGender() const;
    string getPassword() const;

    // display function
    virtual void display() const;
};

// customer class inherits Profile
class Customer : public Profile
{
private:
    string payment_method;

public:
    Customer(const int &id_num, const string &password, const string &name, const string &gender);
    string setPaymentMethod();
    static void viewBooking(BookingInfo &booking_obj);
    static void cancelBooking();
};

class Driver : public Profile
{
private:
    Vehicle *vehicle_obj;

public:
    Driver(const int &id_num, const string &password, const string &name, const string &gender, Vehicle *vehicle_obj);
    string getVehicleType() const;
    void display();
};

// Car, Van and Bike classes inherit Vehicle
class Car : public Vehicle
{
public:
    Car(const string &vehicle_type, const string &color, const string &model, const string &numberplate);
};

class Van : public Vehicle
{
public:
    Van(const string &vehicle_type, const string &color, const string &model, const string &numberplate);
};

class Bike : public Vehicle
{
public:
    Bike(const string &vehicle_type, const string &color, const string &model, const string &numberplate);
};

// abstract class for different payment methods
class PaymentMethod
{
protected:
    string method;

public:
    PaymentMethod(string &method);
    void display() const;
};

// classes Cash and Credit Card inherit PaymentMethod
class Cash : public PaymentMethod
{
public:
    Cash(string &method);
};

class CreditCard : public PaymentMethod
{
private:
    string cardName;
    string expDate;
    int cardNum;

public:
    CreditCard(string &cardName, string &expDate, int &cardNum, string &method);
    void display() const;
};

class TripInfo
{
private:
    string pickup;
    string destination;
    float distance;
    float bill;

public:
    TripInfo(const string &pickup, const string &destination, float distance);
    float estimateBill(const string &vehicle_type);
    void display() const;
};

class BookingInfo
{
private:
    float fare;
    Driver driver_obj;
    PaymentMethod *payment_obj;
    TripInfo trip_info;

public:
    BookingInfo(const Driver &driver_obj, PaymentMethod *payment_obj, const string &pickup, const string &destination, float distance);
    float bill();
    void display();
};

#endif
