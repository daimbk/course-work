# Assignment 2.     Name: Daim Bin Khalid.   Roll no.: 251686775

# Task 1

def left_right():
	string1 = input("Enter first string: ")
	string2 = input("Enter second string: ")
	dot = 50 - (len(string1) + len(string2))    #determines the number of dots to be placed in between strings.
	print(string1 + "{}".format("." * dot) + string2)      #using formatting to sandwich dots in between the two strings.
left_right()


# Task 2

def len_compare():
	string1 = input("Enter first string: ")
	string2 = input("Enter second string: ")
	if len(string1) > len(string2):    #checking if string1 is bigger than string2
		return True
	else:
		return False
len_compare()


# Task 3

def sub_check():
	string1 = input("Enter first string: ")
	string2 = input("Enter second string: ")
	if string2 in string1:      #checking if string2 is present in string1 using in reserved method
		print(True)
	else:
		print(False)
sub_check()


# Task 4

alph = input("Enter an alphabet: ")
while (len(alph) != 1) or (alph.isalpha() == False):      #conditional loop to make sure only alphabet is entered
	alph = input("Wrong input, enter just an alphabet: ")
if (alph in ('a','e','i','o','u')) or (alph in ('A','E','I','O','U')):       #checking if input is vowel or string using in
	print("Vowel")
else:
	print("Consonant")



# Task 5

num_in = int(input("Enter a number upto 3,999: "))

while (num_in) > 3999 or (num_in) < 0:        #making sure input lies between 0 and 4000
	num_in = input("Out of range, enter again: ")

M = ['', 'M', 'MM', 'MMM']                           #defining lists with corresponding unit places
C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
L = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
O = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

thousands = M[num_in // 1000]              #remainder of this operation will be of thousands unit place and access that index in list
hundreds = C[(num_in % 1000) // 100]      #will find the hundreds unit place and get corresponding value from list index
tens = L[(num_in % 100) // 10]
units = O[num_in % 10]              

roman = (thousands + hundreds + tens + units)
print(roman)



# Task 6

import random
word_in = input('Enter a word: ')
for i in range(len(word_in)):
	i = random.randint(0, len(word_in) - 2)
	j = random.randint(i + 1, len(word_in) - 1)

first = word_in[:i]    #first part of string up til i position
middle = word_in[i + 1:j]    #second part of string from i onwards till j
last = word_in[j + 1:i]       #third part of string from j onward till remaining letters back up til i
word_in = first + word_in[j] + middle + word_in[i] + last
print(word_in)



# Task 7

side_len = int(input("Enter side length: "))

for i in range (side_len): 
    full = '*' * side_len         #instead of printing use variables to store boxes
    if i in (0, side_len -1):       #checking if first or last line
        hollow = '*' * side_len
    else:
        hollow = f'*{" " * (side_len - 2) }*'      #use formatting to enter spaces and make hollow lines

    print(f'{full} {hollow}')                #use formatting to print squares next to each other



# Task 8

card_num = input('\nEnter an 8 digit credit-card number: ')

while len(card_num) != 8:
	card_num = input('\nEnter again with 8 digits only: ')

odd_sum = 0
new_sum = 0

for i in range(7, -1, -2):
	odd_sum = odd_sum + int(card_num[i])    #every other number starting from last is added

for y in range(6, -1, -2):
	double = 2 * int(card_num[y])
	double = str(double)
	if len(double) == 2:
		new_sum = new_sum + int(double[0]) + int(double[1])          #every remaining number is double and each subscript is added
	else:
		new_sum = new_sum + int(double[0])

total = odd_sum + new_sum
remainder = total % 10

if remainder == 0:        #checking for correct check digit
	print('Valid')
else:
	last_digit = int(card_num[-1])
	if last_digit - remainder < 0:           #if the check gives a negative value it will be made positive after the if
		check_digit = last_digit + (10 - remainder)
	else:
		check_digit = last_digit - remainder

	print('Invalid, the check digit should be ' + str(check_digit))



# Task 9

num_input = int(input('Enter an integer: '))

for i in range(2, num_input + 1):
    prime_flag = True         #set a flag value for further condition checking
    for x in range(2, i):
        if (i % x == 0):          #to check if each number in loop is divisible by another or not
            prime_flag = False
    if prime_flag == True:
       print(i)