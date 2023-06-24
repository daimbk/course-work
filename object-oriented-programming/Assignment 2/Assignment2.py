# Assignment 2
# Daim Bin Khalid
# 251686775

# Task 1
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print('Name: ' + self.name + '\nID Number: ' + str(self.id))

class Vehicle:
    def __init__(self, manufacturer, cylinders, owner_obj):
        self.manufacturer = manufacturer
        self.cylinders = cylinders
        self.owner = owner_obj     # aggregation with Person class

    def display(self):
        self.owner.display()
        print('Manufacturer: ' + self.manufacturer)
        print('Number of cylinders: ' + str(self.cylinders))

class Truck(Vehicle):
    def __init__(self, manufacturer, cylinders, owner_obj, load_capacity, towing_capacity):
        super().__init__(manufacturer, cylinders, owner_obj)
        self.load_capacity = load_capacity
        self.towing_capacity = towing_capacity

    def display(self):
        print('Truck Information: ')
        super().display()
        print('Load Capacity: ' + str(self.load_capacity) + ' kg')
        print('Towing Capacity: ' + str(self.towing_capacity) + ' kg')
        print()

class Route:
    def __init__(self, travel_time, distance, start_point, destination, fare):
        self.travel_time = travel_time
        self.distance = distance
        self.start_point = start_point
        self.destination = destination
        self.fare = fare

    def display(self):
        print('Start: ' + self.start_point)
        print('Destination: ' + self.destination)
        print('Travel Time: ' + self.travel_time)
        print('Distance: ' + str(self.distance) + ' km')
        print('Fare : Rs. ' + str(self.fare))
        print()

class Bus(Vehicle):
    def __init__(self, manufacturer, cylinders, owner_obj, pass_num, luggage_weight):
        super().__init__(manufacturer, cylinders, owner_obj)
        self.pass_num = pass_num
        self.luggage_weight = luggage_weight

    def display(self):
        print('Bus Information: ')
        super().display()
        print('Number of passengers: ' + str(self.pass_num) + ' passengers')
        print('Luggage Weight: ' + str(self.luggage_weight) + ' kg')
        print()

    def RouteInfo(self, routeobj):
        print('Bus Route: ')
        routeobj.display()

def main():
    print('Task 1: ')
    #setup owners
    ownerslist = []
    owner_obj = Person('Daim', 111)
    ownerslist.append(owner_obj)
    owner_obj = Person('Hafsah', 122)
    ownerslist.append(owner_obj)
    owner_obj = Person('Manal', 134)
    ownerslist.append(owner_obj)
    owner_obj = Person('Mo', 145)
    ownerslist.append(owner_obj)

    # setup multiple routes for buses
    routes_list = []
    routeobj = Route('30 min', 35, 'Airport', 'FC College', 1000)
    routes_list.append(routeobj)
    routeobj = Route('1.5 hours', 250, 'Lahore', 'Faisalabad', 1500)
    routes_list.append(routeobj)
    routeobj =Route('15 min', 15, 'Cavalry Ground', 'FC College', 400)
    routes_list.append(routeobj)

    # setup multiple truck objects
    truck_list = []
    newtruck = Truck('Honda', 4, ownerslist[0], 2000.0, 4000)
    truck_list.append(newtruck)
    newtruck = Truck('Toyota', 6, ownerslist[1], 203.5, 6000)
    truck_list.append(newtruck)

    # setup multiple bus objects
    bus_list = []
    newbus = Bus('Daewoo', 6, ownerslist[2], 40, 100)
    bus_list.append(newbus)
    newbus = Bus('Tesla', 6, ownerslist[3], 45, 150)
    bus_list.append(newbus)

    for i in truck_list:
        i.display()
    import random
    for i in bus_list:
        i.display()
        i.RouteInfo(random.choice(routes_list))

main()


# Task 2

from abc import  abstractmethod
class Player:
    def  __init__(self, name, matches):
        self.name = name
        self.matches = matches

    def display(self):
        print('Name: ' + self.name)
        print('Matches played: ' + str(self.matches))

    @abstractmethod
    def playertype(self):
        self.player_type = None
        print(self.player_type)
        pass

class Batsman(Player):
    def  __init__(self, name, matches):
        super().__init__(name, matches)

        self.totalscore = 0
        self.per_match_score = []
        for i in range(self.matches):
            self.per_match_score.append(int(input('Enter match score: ')))
            self.totalscore += self.per_match_score[i]

    def calculate_avg(self):
        self.average = self.totalscore / self.matches

    def display(self):
        super().display()
        print('Scores for all matches are: ')
        print(self.per_match_score)
        print('Total score: ' + str(self.totalscore))
        print('Average score: ' + str(self.average))

    def playertype(self):
        self.player_type = 'Batsman'
        print(self.player_type)

class Bowler(Player):
    def __init__(self, name, matches, numofwickets):
        super().__init__(name, matches)
        self.numofwickets = numofwickets
        self.per_match_wickets = []
        for i in range(self.matches):
            self.per_match_wickets.append(int(input('Enter match wickets: ')))
        print()

    def display(self):
        super().display()
        print('Total wickets taken: ' + str(self.numofwickets))
        print('Wickets per match: ')
        print(self.per_match_wickets)

    def playertype(self):
        self.player_type = 'Bowler'
        print(self.player_type)

def main2():
    print('Task 2: ')
    name = input('Enter batsman name: ')
    matches = int(input('Enter number of matches played by batsman: '))
    batsmanobj = Batsman(name, matches)
    batsmanobj.calculate_avg()

    print()

    name = input('Enter Bowler name: ')
    matches = int(input('Enter number of matches played by bowler: '))
    numofwickets = int(input('Enter total number of wickets taken by bowler: '))
    bowlerobj = Bowler(name, matches, numofwickets)

    batsmanobj.display()
    batsmanobj.playertype()
    print()
    bowlerobj.display()
    bowlerobj.playertype()
    print()
main2()


# Task 3
class CarbonFootprint: #abstract class
    @abstractmethod
    def getCarbonFootprint(self):
        pass

class Building(CarbonFootprint):
    def __init__(self, plotnum):
        self.plotnum = plotnum
        self.electricbill = float(input('Enter average electric bill per month in Rupees: '))
        self.gasbill = float(input('Enter average natural gas bill per month in  Rupees: '))
        self.electric_price = 8.00    # electric price per kwh
        self.gas_price = 3.00    # price per thousand cubic feet average

    def getInfo(self):
        print('Building: \nPlotnum: ' + str(self.plotnum))

    def getCarbonFootprint(self):
        electricbill = (self.electricbill / self.electric_price) * 1.37  * 12
        # formula: Electricity CO2 emissions in pounds = (average amount of electric bill per month ÷ price per kwh) × electricity emissions factor × months in a year
        gasbill = (self.gasbill / self.gas_price) * 120.61 * 12
        # formula: CO2 emissions in pounds = (average amount of natural gas bill per month ÷ price per thousand cubic feet) × natural gas emissions factor × months in a year
        self.footprint = electricbill + gasbill
        print('Greenhouse gas footprint: ' + str(self.footprint) + ' pounds')

class Car(CarbonFootprint):
    def __init__(self, model):
        self.model = model
        self.miles = float(input('Enter number of miles driven on average by car per week: '))
        self.efficiency = float(input('Enter fuel efficiency of vehicle in miles per gallon (mpg) (Average is 25.7): '))
        self.emission = 19.4  # emission per gallon
        self.other_emission = (100 / 95)      # Emissions of greenhouse gases other than CO2

    def getInfo(self):
        print('Car: \nModel: ' + str(self.model))

    def getCarbonFootprint(self):
        self.footprint = ((self.miles * 52) / self.efficiency) * self.emission * self.other_emission
        # formula: CO2 emissions in pounds = ((number of miles driven per week × weeks in a year) ÷ fuel efficiency per vehicle) × pounds of CO2 emitted per gallon × emissions of greenhouse gases other than CO2
        print('Greenhouse gas footprint: ' + str(self.footprint) + ' pounds')

class Bicycle(CarbonFootprint):
    def __init__(self, type):
        self.type = type
    def getInfo(self):
        print('Bicycle:\nCompany: ' + str(self.type))
    def getCarbonFootprint(self):
        print('Greenhouse gas footprint: 0 pounds')

def main3():
    print('Task 3: ')
    obj_list = []
    buildingobj = Building(127)
    carobj = Car('McLaren')
    cycleobj = Bicycle('BMX')
    obj_list.append(buildingobj)
    obj_list.append(carobj)
    obj_list.append(cycleobj)
    print()

    for i in obj_list:
        i.getInfo()
        i.getCarbonFootprint()
        print()
main3()