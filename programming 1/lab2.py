# Lab2   #Name: Daim Bin Khalid, Roll no.: 251686775

#Task 1

string = "Courage was what it takes to stand up and speak; courage was also what it takes to sit down and listen."
print(string.replace("was","is"))

#Task 2
print("Enter 2 integers:")
num_1 = int(input())
num_2 = int(input())

def add(): 
	print("Sum:", (num_1 + num_2))

add()   

def difference():
	print("The difference is:", (num_1 - num_2))

difference()

def product():
	print("The product is:", (num_1*num_2))

product()

def average():
	print("The average is:", ((num_1+num_2)/2))

average()

def max_min():
	print("Greater number is:", max(num_1, num_2))
	print("Smaller number is:", min(num_1, num_2))

max_min()

#Task 3
print("Enter drive letter:")
drive_let = str(input() + ":\\")
print("Enter the path:")
path = ("\\" + input() + "\\" + input())
print("Enter file name:")
file_name = str("\\" + input())
print(drive_let.title() + path.title() + file_name.title() + (".txt"))

#Task 4
letter_h = "* *\n* *\n***\n* *\n* *\n"
letter_e = "***\n*\n***\n*\n***"
letter_l = "*\n*\n*\n*\n***"
letter_o = "***\n* *\n* *\n* *\n* *\n***"
print(letter_h + letter_e + letter_l + letter_l + letter_o)


#Task 5
print("Enter a string with even characters")
even_string = str(input())
print("Enter a string with odd characters")
odd_string = str(input())
print("First, last and middle characters of even string:", even_string[0], even_string[-1], even_string[(int(len(even_string)/2))])
print("First, last and middle characters of odd string:", odd_string[0], odd_string[-1], odd_string[int(len(odd_string)/2)])


#Task 6
num = input("Enter a number between 1,000 and 999,999 (enter comma in your input): ")
string_list = []

for i in range(len(num)):
	if num[int(i)] != ",":
		string_list.append(num[int(i)])

print(*string_list, sep="")


#Task 7
word = input("Enter a string: ")
reverse = word[::-1]
print(reverse)

#Task 8
number_1 = input("Enter first number:")

temp_1 = 0
temp_2 = 0

number_2 = input("Enter second number:")
temp_1 = number_1
temp_2 = number_2
print("The first number is: ", temp_2)
print("The second number is: ", temp_1)

#Task 9
length = int(input("Enter length of rectangle: "))
height = int(input("Enter height of rectangle: "))
area = length * height
perimeter = (length*2) + (height*2)
print("Area of rectangle is: ", area)
print("Perimeter of rectangle is: ", perimeter)

#Task 10
rep_string = input("Enter a string: ")

for i in range(21):
	print(rep_string)