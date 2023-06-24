# Daim Bin Khalid
# 251686775
# Lab 7

# Q1

class Address:
    def __init__(self, housenum, street, town, city):
        self.housenum = housenum
        self.street = street
        self.town = town
        self.city = city

    def display(self):
        print('Address: ', end = '')
        print(self.housenum, self.street, self.town, self.city)

class Student:
    def __init__(self, id, name, housenum, street, town, city):
        self.id = id
        self.name = name
        self.address = Address(housenum, street, town, city)

    def display(self):
        print('ID: ' + str(self.id) + '\nName: ' + str(self.name))
        self.address.display()

class Staff:
    def __init__(self, id, name, housenum, street, town, city):
        self.id = id
        self.name = name
        self.address = Address(housenum, street, town, city)

    def display(self):
        print('ID: ' + str(self.id) + '\nName: ' + str(self.name))
        self.address.display()

class Faculty:
    def __init__(self, id, name, housenum, street, town, city):
        self.id = id
        self.name = name
        self.address = Address(housenum, street, town, city)

    def display(self):
        print('ID: ' + str(self.id) + '\nName: ' + str(self.name))
        self.address.display()


# Q2

class Bank:
    accounts = []
    def __init__(self, accname, accnum, type, balance):
        self.accname = accname
        self.accnum = accnum
        self.type = type
        self.balance = balance
        Bank.accounts.append(self)

    def deposit(self, balance):
        self.balance += balance
        print('Balance deposited, New Balance:', self.balance)

    def withdraw(self, outbalance):
        self.balance = self.balance - outbalance
        print('Withdrawel successful, New Balance:', self.balance)

    def display_account(self):
        print(self.accnum, self.accname)

    def display_balance(self):
        print('Current Balance: ', self.balance)

def main():

    # Question 1:
    print('Question 1:')
    student = Student(44, 'Daim', 'House 9', 'Service Lane', 'AR Complex', 'Lahore')
    staff = Staff(45, 'Hafsah', 'House 443', 'Street 0', 'Fantasy Land', 'Erohal')
    faculty = Faculty(46, 'Manal', 'House 999', 'Street 6', 'Cavalry Ground', 'Lahore')

    student.display()
    print()
    staff.display()
    print()
    faculty.display()
    print()


    # Question 2:
    print('Question 2:')
    account1 = Bank('Daim', 69, 'Current', 50000)
    account2 = Bank('Hafsah', 238, 'Savings', 49999)

    findacc = int(input('Enter account number to find account: '))
    for i in Bank.accounts:
        if i.accnum == findacc:
            i.display_account()
            check = input('Deposit money? Y or N: ')
            if check == 'Y':
                balance = int(input('Enter amount to deposit: '))
                i.deposit(balance)
                check = input('Withdraw money? Y or N: ')
                if check == 'Y':
                    balance = int(input('Enter amount to withdraw: '))
                    i.withdraw(balance)
            else:
                check = input('Withdraw money? Y or N: ')
                if check == 'Y':
                    balance = int(input('Enter amount to withdraw: '))
                    i.withdraw(balance)

main()