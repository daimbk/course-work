#include "classes.h"
#include <chrono>

// Profile class implementation
Profile::Profile(const int &id_num, const string &password, const string &name, const string &gender)
    : id_num(id_num), password(password), name(name), gender(gender) {}

string Profile::getName() const { return name; }

int Profile::getIdNum() const { return id_num; }

string Profile::getGender() const { return gender; }

string Profile::getPassword() const { return password; }

void Profile::display() const
{
    cout << "Profile Information" << endl;
    cout << "Name: " << name << endl;
    cout << "ID: " << id_num << endl;
    cout << "Gender: " << gender << endl;
}

// Customer class implementation
Customer::Customer(const int &id_num, const string &password, const string &name, const string &gender)
    : Profile(id_num, password, name, gender), payment_method("") {}

// set payment method
// return value will be used to create PaymentMethod class object
string Customer::setPaymentMethod()
{
    cout << "Enter payment method (Cash or Card): ";
    cin >> payment_method;

    // Convert payment_method first letter to uppercase
    payment_method[0] = std::toupper(payment_method[0]);

    // Convert the remaining letters to lowercase
    for (size_t i = 1; i < payment_method.length(); i++)
    {
        payment_method[i] = std::tolower(payment_method[i]);
    }

    return payment_method;
}

void Customer::viewBooking(BookingInfo &booking_obj)
{
    // BookingInfo object is associated to Customer
    booking_obj.display();
}

void Customer::cancelBooking()
{
    cout << "Booking Cancelled" << endl;
}

// Driver class implementation
// inherits Profile
Driver::Driver(const int &id_num, const string &password, const string &name, const string &gender, Vehicle *vehicle_obj)
    : Profile(id_num, password, name, gender), vehicle_obj(vehicle_obj) {}

string Driver::getVehicleType() const
{
    return vehicle_obj->getVehicleType();
}

void Driver::display()
{
    // print driver and vehicle info
    Profile::display();
    vehicle_obj->display();
}

// Vehicle class implementation
Vehicle::Vehicle(const string &vehicleType, const string &color, const string &model, const string &numberPlate)
    : vehicleType(vehicleType), color(color), model(model), numberPlate(numberPlate) {}

string Vehicle::getVehicleType() const { return vehicleType; }

string Vehicle::getColor() const { return color; }

string Vehicle::getModel() const { return model; }

string Vehicle::getNumberPlate() const { return numberPlate; }

void Vehicle::display() const
{
    cout << "Vehicle: " << vehicleType << " " << color << " " << model << endl;
    cout << "Number Plate: " << numberPlate << endl;
}

// Car class implementation
Car::Car(const string &vehicle_type, const string &color, const string &model, const string &numberplate)
    : Vehicle(vehicle_type, color, model, numberplate) {}

// Van class implementation
Van::Van(const string &vehicle_type, const string &color, const string &model, const string &numberplate)
    : Vehicle(vehicle_type, color, model, numberplate) {}

// Bike class implementation
Bike::Bike(const string &vehicle_type, const string &color, const string &model, const string &numberplate)
    : Vehicle(vehicle_type, color, model, numberplate) {}

// PaymentMethod class implementation
PaymentMethod::PaymentMethod(string &method) : method(method) {}

void PaymentMethod::display() const
{
    cout << "Payment Method: " << method << endl;
}

// Cash class implementation
Cash::Cash(string &method) : PaymentMethod(method) {}

// CreditCard class implementation
CreditCard::CreditCard(string &cardName, string &expDate, int &cardNum, string &method)
    : PaymentMethod(method), cardName(cardName), expDate(expDate), cardNum(cardNum) {}

void CreditCard::display() const
{
    PaymentMethod::display();
    cout << "Credit Card Holder: " << cardName << endl;
    cout << "Card Number: " << cardNum << endl;
    cout << "Card Expiry Date: " << expDate << endl;
}

// TripInfo class implementation
// creates data for booking including route details and bill
TripInfo::TripInfo(const string &pickup, const string &destination, float distance)
    : pickup(pickup), destination(destination), distance(distance), bill(0) {}

float TripInfo::estimateBill(const string &vehicle_type)
// function to calculate the bill according to vehicle type and distance of trip
// formula for bill = booking charge + (vehicle factor * total distance)
{
    if (vehicle_type == "Car")
        bill = 150 + (2 * distance);
    else if (vehicle_type == "Van")
        bill = 150 + (1.5 * distance);
    else
        bill = 150 + (1 * distance);
    return bill;
}

void TripInfo::display() const
{
    cout << "Pickup Location: " << pickup << endl;
    cout << "Destination: " << destination << endl;
    cout << "Total Distance: " << distance << endl;
}

// BookingInfo class implementation
/* contains all booking info including:
 route information, bill, driver assigned for trip, method of payment.
 Driver object, PaymentMethod object are aggregated.
 TripInfo object is made by composition */
BookingInfo::BookingInfo(const Driver &driver_obj, PaymentMethod *payment_obj, const string &pickup, const string &destination, float distance)
    : fare(0), driver_obj(driver_obj), payment_obj(payment_obj), trip_info(pickup, destination, distance) {}

float BookingInfo::bill()
{
    fare = trip_info.estimateBill(driver_obj.getVehicleType());
    return fare;
}

void BookingInfo::display()
{
    fare = trip_info.estimateBill(driver_obj.getVehicleType());

    // get current date
    time_t now = std::chrono::system_clock::to_time_t(std::chrono::system_clock::now());
    char buffer[80];
    strftime(buffer, sizeof(buffer), "%d/%m/%Y", localtime(&now));
    string current_date(buffer);

    cout << "Booking Details:" << endl;
    cout << "Date: " << current_date << endl;
    trip_info.display();
    cout << endl;
    cout << "Driver Info:" << endl;
    cout << "Name: " << driver_obj.getName() << "\nGender: " << driver_obj.getGender() << endl;
    driver_obj.display();
    cout << endl;
    cout << "Trip Bill: Rs. " << fare << endl;
    payment_obj->display();
}
