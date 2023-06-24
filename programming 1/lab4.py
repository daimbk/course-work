# Lab 4.    Name: Daim Bin Khalid.  Roll no.: 251686775

# Task 1

max_rows = 10  #defining to set limits
max_column = 10
for i in range(1, max_rows + 1):  #runs for 10 number of rows
	print()
	for x in range(1, max_column + 1):  #runs and prints values for columns
		print(i * x, end = " ")	
print()


# Task 2
for i in range(0, 21): #set upper limit to 21 so upto 20 is used
	print(2 ** i)


# Task 3

odd_sum = 0   #defining var
num_input = input("Enter a number: ")
for i in range(len(num_input)):   #loop runs for the number of characters in the number
	if int(num_input[i]) % 2 != 0:    #condition checking if each number is odd or even
		odd_sum = odd_sum + int(num_input[i])
print(odd_sum)


# Task 4

import random
rand = random.randint(0, 9)   #setting a random number in a variable
for i in range(0,6):   #loop gives 5 attempts if not guessed
	user_in = int(input("Enter your guess of the 1 digit lucky number: "))
	if user_in == rand:     #checking if guess is correct
		print("you win")
		break               #break if guess is correct
	else:
		print("you lost")