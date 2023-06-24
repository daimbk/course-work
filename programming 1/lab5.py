# Lab 5.    Name: Daim Bin Khalid.    Roll no.: 251686775

# Task 1
# To print a diamond of side entered by user.

side_len = int(input("Enter length of side: "))

for index in range(side_len):
	for i in range((side_len - 1) - index):
		print(" ", end = " ")
	for x in range((index * 2) + 1):
		print("*", end = " ")
	print()	                       #Prints top half of diamond by using spacing in first for loop and asteriks in second for loop.
for a in range (side_len - 1, -1, -1):
	for y in range(side_len - a):
		print(" ", end = " ")
	for b in range((a * 2) - 1):
		print("*", end = " ")
	print()                        #Prints lower half of diamond by using spacing in first for loop and asteriks in second for loop.


# Task 2
# Determine the drunkard's final location after moving through 100 random directions at intersections.

x = 0   #initializing drunkard's starting coordinates
y = 0
north = 1    #assigning a value to each direction to determine where he went
south = 2
west = 3
east = 4
import random
for i in range(99):
	move = random.randint(1,4)     #generate a random direction
	if move == 1:              #check x or y coordinate and adjust previous position accordingly
		y = y + 1
	elif move == 2:
	    y = y - 1
	elif move == 3:
	    x = x - 1
	elif move == 4:
	    x = x + 1

print(x, y)


# Task 3
# Print each substring and combination of substrings.

word_in = input("Enter a string: ")
for i in range(1, len(word_in) + 1):           #set up nested for loops to use as indexing in printing individual and combination of string characters.
	for x in range(0, len(word_in) - i + 1):
		print(word_in[x:x+i])