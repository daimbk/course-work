# Lab 8
# Daim Bin Khalid
# 251686775

# Question 1
class Polygon:
    def __init__(self, numOfSides):
        self.numOfSides = numOfSides

    def inputSides(self):
        if self.numOfSides == 3:
            self.length = float(input('Enter length: '))
            self.width = float(input('Enter width: '))
            return self.length, self.width
        elif self.numOfSides == 4:
            self.length = float(input('Enter length: '))
            return self.length

class Triangle(Polygon):
    def __init__(self, numOfSides):
        super().__init__(numOfSides)

    def Area(self):
        self.area = (0.5 * self.length * self.width)
        return self.area

    def display(self):
        print('Area of triangle is ', str(self.area))

class Square(Polygon):
    def __init__(self, numOfSides):
        super().__init__(numOfSides)

    def Area(self):
        self.area = (self.length ** 2)
        return self.area

    def display(self):
        print('Area of square is ', str(self.area))


# Question 2
class Person:
    def __init__(self, PersonID, PersonName):
        self.PersonID = PersonID
        self.PersonName = PersonName

class Patient(Person):
    def __init__(self, PersonID, PersonName, PatientDisease):
        super().__init__(PersonID, PersonName)
        self.PatientDisease = PatientDisease
        self.Treatment = ''

    def chart(self):
        print(self.PersonID, self.PersonName, self.PatientDisease, self.Treatment, sep = '\n')

class Doctor(Person):
    def __init__(self, PersonID, PersonName):
        super().__init__(PersonID, PersonName)

    def treat(self, patientobj):
        patientobj.Treatment = input('Patient ' + patientobj.PersonName + ' is diagnosed with ' + patientobj.PatientDisease + '. Suggest Treatment : ')


def main():

    global shape
    print('Question 1:')
    numsides = int(input('Enter number of sides of polygon (3 or 4): '))
    if numsides == 3:
        shape = Triangle(3)
    elif numsides == 4:
        shape = Square(4)

    shape.inputSides()
    shape.Area()
    shape.display()

    print('Question 2:')
    PatientID = int(input('Enter patient id: '))
    PatientName = input('Enter patient name: ')
    PatientDisease = input('Enter disease: ')
    patientobj = Patient(PatientID, PatientName, PatientDisease)

    doctorID = int(input('Enter doctor id: '))
    doctorName = input('Enter name: ')
    docobj = Doctor(doctorID, doctorName)
    docobj.treat(patientobj)
    patientobj.chart()
main()