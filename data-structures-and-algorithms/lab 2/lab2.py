# Lab 2
# Daim Bin Khalid
# 251686775

# Question 1

words_list = input("Enter list of words: ")
words_list = words_list.split()
words_dictionary = {}

for i in words_list:
    if i not in words_dictionary:
        words_dictionary[i] = 1
    else:
        words_dictionary[i] += 1

for word, count in words_dictionary.items():
    print(word + ' appears ' + str(count) + ' number of times')


# Question 2

class Car:
    def __init__(self, car_make, car_model, model_year, purchase_year, meter_reading, color, price, registration_number,
                 owner_name):
        self.car_make = car_make
        self.car_model = car_model
        self.model_year = model_year
        self.purchase_year = purchase_year
        self.meter_reading = meter_reading
        self.color = color
        self.price = price
        self.registration_number = registration_number
        self.owner_name = owner_name

    def get_owner_name(self):
        return self.owner_name

    def transfer(self, owner_name, meter_reading, purchase_year, price):
        self.owner_name = owner_name
        self.meter_reading = meter_reading
        self.purchase_year = purchase_year
        self.price = price

    def display(self):
        print(
            f'Car Details: {self.color} {self.car_make} {self.car_model}\nModel Year: {self.model_year}\nPurchase Year {self.purchase_year}\nMeter Reading {self.meter_reading}\nRegistration Number: {self.registration_number}\nOwner Name: {self.owner_name}')


class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.vehicle = None

    def get_name(self):
        return self.name

    def set_vehicle(self, car_obj):
        self.vehicle = car_obj


def main():
    car_obj = Car('BMW', 'M4', 2015, 2015, 0, 'White', 1200000, 'LKK22', 'Daim')

    owner_obj = Customer('Daim', 'M')
    owner_obj.set_vehicle(car_obj)

    second_customer = Customer('Kiran', 'F')
    second_customer.set_vehicle('None')

    # print details before transfer
    print()
    car_obj.display()

    # update car details to accommodate new owner
    car_obj.transfer(second_customer.get_name(), 50000, 2018, 1000000)
    second_customer.set_vehicle(car_obj)
    owner_obj.set_vehicle('None')

    # display new car info
    print()
    car_obj.display()


main()


# Question 3

class Polygon:
    def __init__(self):
        self.name = None

    def area(self):
        pass

    def perimeter(self):
        pass

    def get_name(self):
        return self.name


class Triangle(Polygon):
    def __init__(self, first_length, second_length, width, height):
        super().__init__()
        self.name = 'Triangle'
        self.first_length = first_length
        self.second_length = second_length
        self.width = width
        self.height = height

    def area(self):
        return 0.5 * self.width * self.height

    def perimeter(self):
        return self.first_length + self.second_length + self.width


class IsoscelesTriangle(Triangle):
    def __init__(self, first_length, second_length, width, height):
        super().__init__(first_length, second_length, width, height)
        self.name = 'Isosceles Triangle'

    def perimeter(self):
        return 2 * self.first_length + self.width


class EquilateralTriangle(Triangle):
    def __init__(self, first_length, second_length, width, height):
        super().__init__(first_length, second_length, width, height)
        self.name = 'Equilateral Triangle'

    def perimeter(self):
        return 3 * self.first_length


class Quadrilateral(Polygon):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Rectangle(Quadrilateral):
    def __init__(self, length, width):
        super().__init__(length, width)
        self.name = 'Rectangle'


class Square(Quadrilateral):
    def __init__(self, length, width):
        super().__init__(length, width)
        self.name = 'Square'


class Pentagon(Polygon):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.name = 'Pentagon'

    def area(self):
        from math import sqrt

        return (sqrt(5 * (5 + 2 * (sqrt(5)))) * self.length * self.length) / 4

    def perimeter(self):
        return 5 * self.length


class Hexagon(Polygon):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.name = 'Hexagon'

    def area(self):
        import math
        return (3 * math.sqrt(3) * (self.length * self.length)) / 2

    def perimeter(self):
        return 6 * self.length


class Octagon(Polygon):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.name = 'Octagon'

    def area(self):
        import math
        return 2 * (1 + (math.sqrt(2))) * self.length * self.length

    def perimeter(self):
        return 8 * self.length


def main():
    shapes = []

    equilateral_triangle = EquilateralTriangle(12, 12, 12, 5)
    shapes.append(equilateral_triangle)
    isosceles_triangle = IsoscelesTriangle(20, 20, 40, 35)
    shapes.append(isosceles_triangle)
    rectangle = Rectangle(15, 30)
    shapes.append(rectangle)
    square = Square(50, 50)
    shapes.append(square)
    pentagon = Pentagon(14)
    shapes.append(pentagon)
    hexagon = Hexagon(18)
    shapes.append(hexagon)
    octagon = Octagon(20)
    shapes.append(octagon)

    for shape in shapes:
        print(f'Shape: {shape.get_name()}\nArea: {shape.area()}\nPerimeter: {shape.perimeter()}\n')


main()
