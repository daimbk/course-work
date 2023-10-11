# Lab 7
# Name: Daim Bin Khalid
# Roll no.: 251686775

# Lists:

# Task 1

def even_replace():
	evenlist = []
	for i in range(10):
		evenlist.append(input('Enter input for list: '))
	for i in range(10):
		if i % 2 == 0:
			evenlist[i + 1] = 'hello'
	print(evenlist)
even_replace()


# Task 2

def reverse():
	orglist = ['hello', 'darkness', 'my old friend']
	orglist.reverse()
	print(orglist)
reverse()


# Task 3

natlist = []
for i in range(1, 21):
	natlist.append(i)
print(natlist)


# Task 4

randlist = []
import random
for i in range(10):
	randlist.append(random.randint(1, 100))
	for j in range(i):
		if randlist[i] == randlist[j]:
			randlist[i] = random.randint(1, 100)
print(randlist)


# Task 5

numlist = [4, 2, 1, 9, 5, 6]
prod = 1
for i in range(0, len(numlist)):
	prod = prod * numlist[i]
print(prod)


# Dictionaries:

# Task 1

newdict = {"Daim" : "Assassin's Creed", "Manal" : "Left 4 Dead 2", "Momi" : "FIFA"}
name = input("Enter a key: ")
if name not in newdict:
	newdict[name] = "Spider Man"
print(newdict)


# Task 2

firstdict = {1 : 'first', 2 : 'second'}
secdict = {3 : 'third', 4 : 'fourth'}
firstdict.update(secdict)
print(firstdict)


# Task 3

n = int(input('Enter number n: '))
square = {}
for i in range(1 , n + 1):
	square.update({i : i * i})
print(square)


# Task 4

iterate =  {1:'a',2:'b',3:'c',4:'d'}
for key, value in iterate.items():
	print(key, iterate[key])