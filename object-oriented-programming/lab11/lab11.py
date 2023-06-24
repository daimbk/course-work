# Lab 11
# Daim Bin Khalid
# 251686775

class Passenger:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def purchase_seat(self, seat_num, bus_obj):
        for seat_obj in bus_obj.get_seats():
            values = seat_obj.get_info()
            if (values[0] == seat_num) and (values[1] == 1):
                seat_obj.set_occupant(self)
                seat_obj.set_availability_flag()
                bus_obj.add_to_total_amount()


class Bus:
    def __init__(self, ticket_price):
        self.ticket_price = ticket_price
        self.total_booking_amount = 0

        # creating 24 seat objects
        self.seats_list = []
        for i in range(24):
            seat_obj = Seat(i)
            seat_obj.set_occupant('')
            self.seats_list.append(seat_obj)

    def add_to_total_amount(self):
        self.total_booking_amount += self.ticket_price

    def get_seats(self):
        # return list of seat objects
        return self.seats_list

    def display(self):
        for i in self.seats_list:
            i.display()


class Seat:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.availability_flag = 1
        self.occupant = ''

    def set_occupant(self, passenger_obj):
        self.occupant = passenger_obj

    def get_occupant(self):
        return self.occupant

    def set_availability_flag(self):
        self.availability_flag = 0

    def get_info(self):
        return self.seat_number, self.availability_flag

    def display(self):
        if self.availability_flag == 0:
            print('Name:', self.occupant.get_name(), '\nSeat Number:', self.seat_number)


def main():
    daewoo_lahore = Bus(1500)
    daim_obj = Passenger('Daim Bin Khalid')
    manal_obj = Passenger('Manal Abbas')

    daim_obj.purchase_seat(15, daewoo_lahore)
    manal_obj.purchase_seat(15, daewoo_lahore)

    daewoo_lahore.display()


main()
