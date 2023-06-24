# Project: Cab Booking System
# Daim Bin Khalid
# 251686775


# abstract class for user type
class Profile:
    def __init__(self, id_num, password, name, gender):
        self.name = name
        self.id_num = id_num
        self.gender = gender
        self.password = password

    # getter functions
    def get_id(self):
        return self.id_num

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    # display profile information
    def display(self):
        print('Profile Information:\nName: ', self.name, '\nID: ', self.id_num, '\nGender: ', self.gender)


# Customer class inherits Profile class
class Customer(Profile):
    def __init__(self, id_num, password, name, gender):
        super().__init__(id_num, password, name, gender)
        self.method = None

    # customer can set their payment method
    def set_payment_method(self):
        """ customer will set their preferred payment method. The return value will later be used to create PaymentMethod class object"""
        self.method = input('Enter payment method (Cash or Credit Card): ').strip(' ').capitalize()
        return self.method

    @staticmethod
    def view_booking(booking_obj):
        """ the function is called when customer wants to view their cab booking. calls BookingInfo object's display"""
        # BookingInfo object is associated to Customer
        booking_obj.display()

    @staticmethod
    def cancel_booking():
        # prints that booking is cancelled
        print('Booking Cancelled')


# Driver class inherits Profile class
class Driver(Profile):
    def __init__(self, id_num, password, name, gender, vehicle_obj):
        super().__init__(id_num, password, name, gender)
        # vehicle object is aggregated to Driver class
        self.vehicle_obj = vehicle_obj

    def get_vehicle_type(self):
        return self.vehicle_obj.get_vehicle_type()

    def vehicle_display(self):
        """ prints driver's profile info along with their vehicle's info"""
        self.vehicle_obj.display()


# abstract class for various vehicle types
class Vehicle:
    def __init__(self, vehicle_type, color, model, numberplate):
        self.vehicle_type = vehicle_type
        self.color = color
        self.model = model
        self.numberplate = numberplate

    # getter functions
    def get_vehicle_type(self):
        return self.vehicle_type

    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

    def get_plate(self):
        return self.numberplate

    def display(self):
        # displays vehicle info
        print('Vehicle:', self.vehicle_type, self.color, self.model)
        print('Number Plate:', self.numberplate)


# Car, Van and Bike classes inherit Vehicle
class Car(Vehicle):
    def __init__(self, vehicle_type, color, model, numberplate):
        super().__init__(vehicle_type, color, model, numberplate)


class Van(Vehicle):
    def __init__(self, vehicle_type, color, model, numberplate):
        super().__init__(vehicle_type, color, model, numberplate)


class Bike(Vehicle):
    def __init__(self, vehicle_type, color, model, numberplate):
        super().__init__(vehicle_type, color, model, numberplate)


# abstract class for different payment methods
class PaymentMethod:
    # user's preferred method is passed to the constructor
    def __init__(self, method):
        self.method = method

    def display(self):
        print('Payment Method:', self.method)


# classes Cash and Credit Card inherit PaymentMethod
class Cash(PaymentMethod):
    def __init__(self, method):
        super().__init__(method)


class CreditCard(PaymentMethod):
    # credit card info of user is passed to the constructor
    def __init__(self, card_name, expiry_date, card_number, method):
        super().__init__(method)
        self.card_name = card_name
        self.expiry_date = expiry_date
        self.card_number = card_number

    def display(self):
        """displays method of payment and credit card info"""
        super().display()
        print('Credit Card Holder:', self.card_name, '\nCard Number:', self.card_number)
        print('Card Expiry Date: ' + self.expiry_date)


class TripInfo:
    # creates data for booking including route details and bill
    # class object will be created in BookingInfo class as a composition relation
    def __init__(self, pickup, destination, distance):
        self.pickup = pickup
        self.destination = destination
        self.distance = distance
        self.bill = None

    def estimate_bill(self, vehicle_type):
        # function to calculate the bill according to vehicle type and distance of trip
        # formula for bill = booking charge + (vehicle factor * total distance)
        if vehicle_type == 'Car':
            self.bill = 150 + (2 * self.distance)
        elif vehicle_type == 'Van':
            self.bill = 150 + (1.5 * self.distance)
        else:
            self.bill = 150 + (1 * self.distance)
        return self.bill

    def display(self):
        # displays route info
        print('Pickup Location:', self.pickup, '\nDestination:', self.destination, '\nTotal Distance:', self.distance,
              'km')


class BookingInfo:
    """ contains all booking info including:
    Route information, bill, driver assigned for trip, method of payment
    Driver object, PaymentMethod object are aggregated
    TripInfo object is made by composition
    """

    def __init__(self, driver_obj, payment_obj, pickup, destination, distance):
        self.fare = None
        self.driver_obj = driver_obj
        self.payment_obj = payment_obj
        self.trip_info = TripInfo(pickup, destination, distance)

    def bill(self):
        # get trip bill by calling TripInfo estimate_bill() function
        self.fare = self.trip_info.estimate_bill(self.driver_obj.get_vehicle_type())
        return self.fare

    def display(self):
        # get trip bill by calling TripInfo estimate_bill() function to display it
        self.fare = self.trip_info.estimate_bill(self.driver_obj.get_vehicle_type())

        # get current date
        from datetime import date
        current_date = date.today()
        current_date = current_date.strftime("%d/%m/%Y")

        print('Booking Details:')
        print('Date:', current_date)
        # user TripInfo object's display function to display its attributes
        self.trip_info.display()
        print()
        print('Driver Info:')
        print('Name:', self.driver_obj.get_name(), '\nGender:', self.driver_obj.get_gender())
        self.driver_obj.vehicle_display()
        print()
        print('Trip Bill: Rs.', self.fare)
        # calls PaymentMethod object's display
        self.payment_obj.display()


# profile functions:
# creating an account for user
def create_profile(user_type, uniqueid):
    profile_file = open(user_type + '.txt', 'a+')
    already_exists = False
    for line in profile_file:
        id_num = line.split(',')
        if uniqueid == id_num[0]:
            print('User with this id already exists.')
            already_exists = True
            profile_file.close()
    if not already_exists:
        name = input('Enter your full name: ')
        gender = input('Gender (M/F/O): ')
        password = input('Enter password: ')
        # generated user data is stored in file
        print(str(uniqueid), password, name, gender, sep=',', file=profile_file)
        profile_file.close()
        # return the attributes required to create user object
        return uniqueid, password, name, gender


# singing in user to their account
def signin(user_type, uniqueid, password):
    profile_file = open(user_type + '.txt', 'r')
    for line in profile_file:
        line = line.rstrip('\n')
        line = line.split(',')
        if (uniqueid == int(line[0])) and (password == line[1]):
            print()
            print('Welcome back', line[2])
            profile_file.close()
            # return the attributes from file required to create user object
            return int(line[0]), line[1], line[2], line[3]


# edit user's profile
def edit_profile(user_type, uniqueid, option, change):
    """var:
    user_type: used to open file depending on if user is customer or driver
    uniqueid: will be matched with existing data while reading profile data from file
    option: will signify what part of profile user wants to modify
    change: new changed data user will provide"""
    profiles = []
    # open file in read mode and store all data in list to make it mutable
    user_file = open(user_type + '.txt', 'r')
    for line in user_file:
        line = line.rstrip('\n').split(',')
        profiles.append(line)
    user_file.close()

    # edit user's data
    # options:
    # 1: user changing their password
    # 2: user changing name
    # 3: user changing gender
    for profile in profiles:
        if int(profile[0]) == uniqueid:
            if option == 1:
                profile[1] = change
            elif option == 2:
                profile[2] = change
            else:
                profile[3] = change

    # write the new data in file
    write_file = open(user_type + '.txt', 'w')
    for profile in profiles:
        print(profile[0], profile[1], profile[2], profile[3], sep=',', file=write_file)
    write_file.close()

    print('Profile Modified')
    print()


# first menu when program starts
def base_menu():
    print('Menu:\n\t1. Sign In\n\t2. Create Profile')
    select = int(input('Enter Option: '))
    while (1 <= select <= 2) is False:
        select = int(input('Option out of range. Enter again: '))

    return select


def generate_id():
    # function to generate a randomized 5 digit id number
    from random import randint

    range_start = 10 ** (5 - 1)
    range_end = (10 ** 5) - 1
    new_id = randint(range_start, range_end)
    return new_id


# menu called when user is customer
def customer_menu(user_type):
    select = base_menu()

    if select == 1:
        # signing in user
        uniqueid = int(input('Enter your id: '))
        password = input('Enter password: ')
        credentials = signin(user_type, uniqueid, password)
        profile_obj = Customer(credentials[0], credentials[1], credentials[2], credentials[3])
        profile_obj.display()

        # new menu to be made here with view history
        booking_done = False
        while not booking_done:
            print(
                'Profile Menu:\n\t1. Book Ride\n\t2. View Booking History\n\t3. Search Booking by Date\n\t4. Edit Profile\n\t5. Exit Menu')
            check = int(input('Enter Option: '))

            # check if input is within limits
            while (1 <= check <= 5) is False:
                check = int(input('Option out of range. Enter again: '))

            # condition executing Book Ride Option
            if check == 1:

                payment_method = profile_obj.set_payment_method()
                # make PaymentMethod object according to user's choice
                if payment_method == 'Cash':
                    payment_obj = Cash(payment_method)
                else:
                    card_name = input('Enter Credit Card holder name: ').title()
                    expiry_date = input('Enter card expiry date (MM/YY): ')
                    card_number = int(input('Enter credit card number: '))
                    payment_obj = CreditCard(card_name, expiry_date, card_number, payment_method)

                # take information for customer of their preferred cab booking details
                vehicle_type = input('What type of vehicle? (Car, Van or Bike): ').capitalize()
                pickup = input('Enter pickup point: ')
                destination = input('Enter destination: ')
                distance = float(input('Enter distance of journey in km: '))

                # check for exact type of available driver's with customer's preferred vehicle
                driver_file = open('driver.txt', 'r')
                vehicle_file = open('vehicles.txt', 'r')
                drivers_list = []

                for line in vehicle_file:
                    line = line.rstrip('\n')
                    line = line.split(',')
                    id_num = line[0]
                    vehicle = line[1]
                    if vehicle_type == vehicle:
                        # put drivers with the requested vehicle in a list
                        drivers_list.append(id_num)

                import random
                # select a driver from list of drivers for booking
                driver_id = random.choice(drivers_list)

                # bring cursor to start of driver file
                driver_file.seek(0)
                vehicle_file.seek(0)

                # initialize vehicle attributes to amend later
                vehicle_color = None
                vehicle_model = None
                vehicle_plates = None

                # set vehicle attributes to create vehicle object
                for line in vehicle_file:
                    line = line.rstrip('\n')
                    line = line.split(',')
                    if line[0] == driver_id:
                        # vehicle_type is already set
                        vehicle_color = line[2]
                        vehicle_model = line[3]
                        vehicle_plates = line[4]

                for read in driver_file:
                    read = read.strip('\n')
                    read = read.split(',')
                    if driver_id == read[0]:

                        # make vehicle object according to vehicle type
                        if vehicle_type == 'Car':
                            vehicle_obj = Car(vehicle_type, vehicle_color, vehicle_model, vehicle_plates)
                        elif vehicle_type == 'Van':
                            vehicle_obj = Van(vehicle_type, vehicle_color, vehicle_model, vehicle_plates)
                        else:
                            vehicle_obj = Bike(vehicle_type, vehicle_color, vehicle_model, vehicle_plates)

                        password = read[1]
                        name = read[2]
                        gender = read[3]
                        driver_obj = Driver(driver_id, password, name, gender, vehicle_obj)

                        # use all the created information to create booking object
                        #  attributes to pass BookingInfo object: driver_obj, payment_obj, pickup, destination, distance, vehicle_obj
                        booking_obj = BookingInfo(driver_obj, payment_obj, pickup, destination, distance)
                        profile_obj = Customer(credentials[0], credentials[1], credentials[2], credentials[3])

                        # setup flag for loop
                        exit_menu = False
                        # cancelled flag indicates if booking would be logged or not
                        cancelled = False
                        while not exit_menu:
                            # loop continues till user wants to exit menu which makes flag True
                            # offer option to customer to view booking or cancel it
                            print('Booking Menu:\n\t1. View Booking\n\t2. Cancel Booking\n\t3. Exit Menu')
                            option = int(input('Enter Option: '))

                            # check if input is within limits
                            while (1 <= option <= 3) is False:
                                option = int(input('Option out of range. Enter again: '))

                            back = False
                            # loop will execute option then break if flag is True
                            while not back:
                                if option == 1:
                                    print()
                                    profile_obj.view_booking(booking_obj)
                                    print()
                                    back = True
                                elif option == 2:
                                    print()
                                    # show that booking is cancelled
                                    profile_obj.cancel_booking()
                                    # returns a flag showing booking is cancelled, so it's not stored in file
                                    cancelled = True
                                    # end parent loop
                                    exit_menu = True
                                    break
                                else:
                                    # end loop
                                    back = True
                                    # end parent loop
                                    exit_menu = True
                                    # end grand-parent loop
                                    booking_done = True

                        # store customer's booking info in their separate file to keep log
                        if not cancelled:
                            # set current date in booking
                            from datetime import date
                            current_date = date.today()
                            current_date = current_date.strftime("%d/%m/%Y")

                            booking_file = open(str(profile_obj.get_id()) + '.txt', 'a+')
                            print(pickup, destination, distance, round(booking_obj.bill(), 2), driver_obj.get_id(),
                                  driver_obj.get_name(), vehicle_obj.get_vehicle_type(), vehicle_obj.get_model(),
                                  vehicle_obj.get_plate(), current_date, sep=',', file=booking_file)

                            # update the driver's number of trips counter and their total earnings in their file
                            previous_earning = [0, 0]
                            # extract previous records from their file first then write after updating in list
                            # open file in read format to extract data to list
                            driver_earning_readfile = open(str(driver_obj.get_id()) + 'earnings.txt', 'a+')
                            driver_earning_readfile.seek(0)
                            if driver_earning_readfile.readline() != '':
                                driver_earning_readfile.seek(0)
                                for line in driver_earning_readfile:
                                    line = line.strip('\n')
                                    line = line.split(',')
                                    previous_earning[0] = int(line[0])
                                    previous_earning[1] = float(line[1])
                            driver_earning_readfile.close()

                            # update data: add 1 to trip counter and 80% of fare as driver's salary
                            previous_earning[0] += 1
                            previous_earning[1] += round(0.8 * booking_obj.bill(), 2)

                            # open file in write format to enter updated trip numbers and earning from list
                            driver_earnings_file = open(str(driver_obj.get_id()) + 'earnings.txt', 'w+')
                            print(str(previous_earning[0]), str(previous_earning[1]), sep=',',
                                  file=driver_earnings_file)

                            # store trip details in driver's file to keep trip record
                            driver_trip_file = open(str(driver_obj.get_id() + '.txt'), 'a+')
                            print(current_date, pickup, destination, distance, round(booking_obj.bill(), 2), uniqueid, credentials[2], credentials[3], sep=',', file=driver_trip_file)

                            driver_trip_file.close()
                            booking_file.close()
                            driver_earnings_file.close()
                            print('Booking Confirmed')

                driver_file.close()
                vehicle_file.close()

            # condition executing View Booking History option
            elif check == 2:
                # exception handling in case file does not exist
                try:
                    booking_file = open(str(uniqueid) + '.txt', 'r')
                    count = 1
                    for line in booking_file:
                        line = line.strip('\n')
                        line = line.split(',')
                        print('Booking ', count, ':', sep='')
                        print('\tDate:', line[9])
                        print('\tPickup:', line[0])
                        print('\tDestination:', line[1])
                        print('\tDistance:', line[2])
                        print('\tFare:', line[3])
                        print()
                        print('\tDriver Name:', line[5])
                        print('\tVehicle:', line[6], line[7])
                        print('\tNumber Plate:', line[8])
                        print()
                        count += 1

                    booking_file.close()

                except FileNotFoundError:
                    print()
                    print('No trips completed yet. File does not exist.')
                    print()
                    booking_done = True

            # executes Search Booking by Date option
            elif check == 3:
                # exception handling in case file does not exist
                try:
                    search_date = input('Enter date to search booking (DD/MM/YYYY): ')
                    booking_file = open(str(uniqueid) + '.txt', 'r')
                    for line in booking_file:
                        line = line.strip('\n')
                        line = line.split(',')
                        if search_date == line[9]:
                            print('Booking Info:')
                            print('\tDate:', line[9])
                            print('\tPickup:', line[0])
                            print('\tDestination:', line[1])
                            print('\tDistance:', line[2])
                            print('\tFare:', line[3])
                            print()
                            print('\tDriver Name:', line[5])
                            print('\tVehicle:', line[6], line[7])
                            print('\tNumber PLate:', line[8])
                            print()

                    booking_file.close()

                except FileNotFoundError:
                    print()
                    print('No trips completed yet. File does not exist.')
                    print()
                    booking_done = True

            # executes Edit Profile option
            elif check == 4:
                print('What do you want to modify?\n\t1. Password\n\t2. Name\n\t3. Gender')
                option = int(input('Enter Option: '))

                # check if input is within limits
                while (1 <= option <= 3) is False:
                    option = int(input('Option out of range. Enter again: '))

                if option == 1:
                    change = input('Enter new password: ')
                elif option == 2:
                    change = input('Enter new name: ')
                else:
                    change = input('Enter gender: ')

                edit_profile(user_type, uniqueid, option, change)

            # exit menu option
            else:
                break

    elif select == 2:
        # credentials will have tuple of returned values having user attributes
        credentials = create_profile(user_type, generate_id())

        # the generated id from function will be passed to create_profile function
        profile_obj = Customer(credentials[0], credentials[1], credentials[2], credentials[3])
        print()
        profile_obj.display()


# menu called when user is a driver
def driver_menu(user_type):
    select = base_menu()

    # initialize variable to be used later
    vehicle_obj = None

    if select == 1:
        # signing in user
        uniqueid = int(input('Enter your id: '))
        password = input('Enter password: ')
        credentials = signin(user_type, uniqueid, password)
        profile_obj = Driver(credentials[0], credentials[1], credentials[2], credentials[3], vehicle_obj)
        profile_obj.display()

        exit_menu = False
        while not exit_menu:
            print('Profile Menu:\n\t1.View Total Earnings\n\t2. View Trips History\n\t3. Search Booking by Date\n\t4. Edit Profile\n\t5. Exit Menu')
            option = int(input('Enter Option: '))

            # check if input is within limits
            while (1 <= option <= 5) is False:
                option = int(input('Option out of range. Enter again: '))

            # setup up a nested loop to come back to Profile Menu after executing option
            back = False
            while not back:
                # execute first option
                if option == 1:
                    # exception handling in case file does not exist
                    try:
                        driver_earnings = open(str(uniqueid) + 'earnings.txt', 'r')
                        for line in driver_earnings:
                            line = line.strip('\n')
                            line = line.split(',')
                            print()
                            print('Trips Completed:', line[0])
                            print('Total Earning: Rs.', line[1])
                        driver_earnings.close()
                        back = True

                    except FileNotFoundError:
                        print()
                        print('No trips completed yet. File does not exist.')
                        print()
                        back = True

                # executes second option
                elif option == 2:
                    # exception handling in case file does not exist
                    try:
                        driver_trip_history = open(str(uniqueid) + '.txt', 'r')
                        count = 1
                        for line in driver_trip_history:
                            line = line.strip('\n')
                            line = line.split(',')
                            print()
                            print('Booking ', count, ':', sep='')
                            print('\tDate:', line[0])
                            print('\tPickup:', line[1])
                            print('\tDestination:', line[2])
                            print('\tDistance:', line[3])
                            print('\tFare:', line[4])
                            print('\tCustomer:', line[6])
                            print('\tGender:', line[7])
                            count += 1
                        driver_trip_history.close()
                        back = True

                    except FileNotFoundError:
                        print()
                        print('No trips completed yet. File does not exist.')
                        print()
                        back = True

                # executes third option
                elif option == 3:
                    # exception handling in case file does not exist
                    try:
                        search_date = input('Enter date to search booking (DD/MM/YYYY): ')
                        driver_trip_history = open(str(uniqueid) + '.txt', 'r')
                        for line in driver_trip_history:
                            line = line.strip('\n')
                            line = line.split(',')
                            if search_date == line[0]:
                                print('Booking Info:')
                                print('\tDate:', line[0])
                                print('\tPickup:', line[1])
                                print('\tDestination:', line[2])
                                print('\tDistance:', line[3])
                                print('\tFare:', line[4])
                                print('\tCustomer:', line[6])
                                print('\tGender:', line[7])

                        driver_trip_history.close()
                        back = True

                    except FileNotFoundError:
                        print()
                        print('No trips completed yet. File does not exist.')
                        print()
                        back = True

                # executes Edit Profile option
                elif option == 4:
                    print('What do you want to modify?\n\t1. Password\n\t2. Name\n\t3. Gender')
                    option = int(input('Enter Option: '))

                    # check if input is within limits
                    while (1 <= option <= 3) is False:
                        option = int(input('Option out of range. Enter again: '))

                    if option == 1:
                        change = input('Enter new password: ')
                    elif option == 2:
                        change = input('Enter new name: ')
                    else:
                        change = input('Enter gender: ')

                    edit_profile(user_type, uniqueid, option, change)
                    back = True

                else:
                    # flags are made True to exit loop and parent loop
                    exit_menu = True
                    back = True

    elif select == 2:
        # creating profile for user

        # the id will be passed to create_profile function
        id_num = generate_id()

        # take driver's vehicle info
        vehicle_type = input('Enter your vehicle type (Car, Van or Bike: ').capitalize()
        vehicle_color = input('Enter vehicle color: ').capitalize()
        vehicle_model = input('Enter name/model: ').title()
        vehicle_plate = input('Enter number plate: ').upper()

        # store driver's vehicle info in file with their id number
        vehicle_file = open('vehicles.txt', 'a+')
        print(id_num, vehicle_type, vehicle_color, vehicle_model, vehicle_plate, sep=',', file=vehicle_file)
        vehicle_file.close()

        # create vehicle object according to owner's vehicle type
        if vehicle_type == 'Car':
            vehicle_obj = Car(vehicle_type, vehicle_color, vehicle_model, vehicle_plate)
        elif vehicle_type == 'Van':
            vehicle_obj = Van(vehicle_type, vehicle_color, vehicle_model, vehicle_plate)
        else:
            vehicle_obj = Bike(vehicle_type, vehicle_color, vehicle_model, vehicle_plate)

        credentials = create_profile(user_type, id_num)

        # make driver object with corresponding vehicle object
        profile_obj = Driver(credentials[0], credentials[1], credentials[2], credentials[3], vehicle_obj)
        print()
        profile_obj.display()


def main():
    print("Welcome to Daim's Cab Service")

    # input if user is customer or driver
    user_type = input('Customer or Driver: ').lower()

    # keep prompting user if input is incorrect
    while (user_type != 'customer') and (user_type != 'driver'):
        user_type = input('Incorrect input. Enter Customer or Driver: ').lower()

    # call customer menu if user is customer
    if user_type == 'customer':
        customer_menu(user_type)

    # call driver menu if user is driver
    elif user_type == 'driver':
        driver_menu(user_type)


main()
