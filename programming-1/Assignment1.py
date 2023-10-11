# Assignment 1.  Name : Daim Bin Khalid, Roll Number : 251686775


# Task 1

'''Used \n command to print numbers in seperate lines'''

print(1,2,3,4, sep = "\n\n")


# Task 2

'''String related commands such as .upper() are used to capitalise letters.
Indexing used on strings to get particular characters.
'''

string1 = "abcd"
print(string1[0].upper() + string1[2])
string2 = "9"
print(string2.replace("9","57"))  #Replaced 9 with 57
string3 = "PythonAssignment"
print(string3[2] + string3[4] + string3[6])
print(string3[8:1:-1])  #Used reverse indexing to print string in a particular order
print(string3[12].upper() + string3[13])


# Task 3

'''Printing comb thrice then adding a bottom line seperately makes a complete grid for tic-tac-toe.'''

comb = "\n+--+--+--+\n|  |  |  |"
last_line = "\n+--+--+--+"
print(comb*3 + last_line)


# Task 4

'''The division per ingredient requirement gives minimum requirement per burger. 
Then check the minimum number of ingredient needed through min() function.
'''

meat = int(input("Enter the number of chicken meats: "))
lettuce = int(int(input("Enter the number of lettuce leaves: ")) / 3)
tomato = int(int(input("Enter the number of tomato slices: ")) / 6)
burger = min(meat, lettuce, tomato)
print(str(burger) + " is the number of burgers that can be made.")


# Task 5

'''Used .lstrip() function on the string to remove whitespace'''

white_string =  "     Programming is fun :-)"
white_string = white_string.lstrip()
print(white_string)


# Task 6

'''The time will be entered in military format then checked for validity of range through if statements.
The difference is then calculated and displayed with abs() function to avoid negative values.
'''

first_time = input("Enter the first time: ")
sec_time = input("Enter the second time: ")
if (int(first_time[0]) > 2) or (int(first_time[2]) > 5):
	first_time = input("First time is incorrect, enter again: ")

if (int(sec_time[0]) > 2) or (int(sec_time[2]) > 5):
	sec_time = input("Second time is incorrect, enter again: ")	

diff_hour = int(sec_time[0] + sec_time[1]) - int(first_time[0] + first_time[1])
diff_minute = int(sec_time[2] + sec_time[3]) - int(first_time[2] + first_time[3])
print(str(abs(diff_hour)) + " hours and " + str(abs(diff_minute)) + " minutes")