# Lab 10
# Name: Daim Bin Khalid
# Roll no. : 251686775


# Task 1

import random
floatnum = float(random.uniform(0, 100))

num = int(floatnum)
conv = str(random.randint(0, 100))
print(2 + 2 * 2)


# Task 2

nat_num = int(input('Enter a natural number:\n' ))

while nat_num < 0:
	nat_num = int(input('Incorrect, enter only natural number:\n' ))

print(nat_num ** 20)


# Task 3

gallon = float(input('Enter fuel amount in gallons: '))

trav = (12 * (3.79 * gallon))
msg = 'Car can travel ' + str(trav) + ' with this fuel.'
remaining = 377.2 - trav

if remaining < 0:
	print(msg + '\nCar can travel ' + str(abs(remaining)) + ' extra KMs after destination.')
elif remaining > 0:
	print(msg + '\nCar needs ' + str(remaining / 12) + ' more litres of fuel to reach destination.')


# Task 4

def amplifier(frequency, number):
	return(frequency * number)

amplifier(60, 3)


# Task 5

teen_list = []
def check(agelist):
	for i in range(5):
		if agelist[i] > 12 and agelist[i] < 20:
			teen_list.append(agelist[i])
	print(teen_list)

check([55, 33, 3, 16, 13])


# Task 6

word_in = input("Enter a string: ")
for i in range(1, len(word_in) - 1):
	for x in range(0, len(word_in) - i + 1):
		print(word_in[x : x + i])


# Task 7 picture submitted in zip file

# Task 8

list_nat = [1,2,3,4,5,6,7,8,9,10]
list_even = [2,4,6,8,10,12,14,16,18,20]
common = []
for i in range(10):
	for x in range(10):
		if list_even[x] == list_nat[i]:
			common.append(list_nat[i])

print(common)


# Task 9

data = {
	'employee1' : {'Name' : 'John', 'Department' : 'Sales', 'Salary' : 1500},
	'employee2' : {'Name' : 'Kieth', 'Department' : 'IT', 'Salary' : 7500},
	'employee3' : {'Name' : 'Shane', 'Department' : 'Sales', 'Salary' : 3450},
	'employee4' : {'Name' : 'Damien', 'Department' : 'Accounting', 'Salary' : 5000},
	'employee5' : {'Name' : 'Courtney', 'Department' : 'Acting', 'Salary' : 6000}
}

def min(data):
	lowest = 1000000
	for i in data:
		if data[i]['Salary'] < lowest:
			lowest = data[i]['Salary']
	print(lowest)	

min(data)

def max(data):
	max = 0 
	for i in data:
		if data[i]['Salary'] > max:
			max = data[i]['Salary']
	print(max)	

max(data)