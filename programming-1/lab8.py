# Lab 8.            Name: Daim Bin Khalid.          Roll no.: 251686775.

# Lists

# Task 1

list1 = ['apple', 'orange', 'banana', 'pineapple']

def find(element, list):
	print(list1.index(element))

find('banana', list1)


# Task 2

import random

first_name = ['Daim', 'Manal', 'Momi', 'Julia', 'Hafsa', 'Kiran']
last_name = ['Bin Khalid', 'Ammad', 'Raza',  'Sarah', 'Shahbaz', 'Qaiser']
rand_num = random.randint(1, 36)

def randomness(first_name, last_name, rand_num):
	for i in range(rand_num - 1):
		print(first_name[random.randint(0,5)], last_name[(random.randint(0,5))], sep = ' ', end = ', ')

	print(first_name[random.randint(0,5)], last_name[(random.randint(0,5))], sep = ' ')	

randomness(first_name, last_name, rand_num)


# Task 3

subjects = ['Computer', 'Basic Electronics', 'WRCM']
credithrs = [4, 4, 3]

def combine(subjects, credithrs):
	print(*tuple(zip(subjects, credithrs)))

combine(subjects, credithrs)


# Task 4

num_list = [7, -9, 87, -65, -44, 456]

def neg_remove(num_list):
	for i in range(6):
		if num_list[i] < 0:
			num_list[i] = 'a'
	while 'a' in num_list:
		num_list.remove('a')
	print(num_list)

neg_remove(num_list)


# Task 5

list_num = [8, 1, 2, 5, 10, 4]

def min_max(list_num):
	minimum = min(list_num)
	maximum = max(list_num)
	print('Minimum: ', minimum, 'Index: ', list_num.index(minimum))
	print('Maximum: ', maximum, 'Index: ', list_num.index(maximum))

min_max(list_num)


# Dictionaries

# Task 1

P_Dictionary = {'Daim' : 3432424, 'Manal' : 2489898, 'Momi' : 9084357, 'Julia' : 311231, 'Hafsa' : 7932479, 'Kiran' : 123133, 'Arbab' : 9874723, 'Omer' : 324244, 'Danyal' : 879832, 'Hehe' : 2132847}
print(P_Dictionary)


# Task 2 and 3

def add(dictionary, name, phone):
	if name in P_Dictionary:
		print('Already exists')
	else:	
		P_Dictionary[name] = phone
		print('Added')

add(P_Dictionary, 'Ali', 242142)


# Task 4

def Delete(dictionary, name):
	if name in P_Dictionary:
		P_Dictionary.pop(name)
	else:
		print('Not found!')

Delete(P_Dictionary, 'Wuhao')