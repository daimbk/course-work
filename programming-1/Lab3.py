# Lab 3.     Name: Daim Bin Khalid.  Roll No.: 251686775

# Task 1

def fav_movie(movie = "Spider Man"):
	'''This function prompts user input for favourite movie.
	If no input is provided then Spider Man is printed.

	variable:
	movie -> default string variable
	movie2 -> user input string
	'''
	
	movie2 = input("Enter your favourite movie: ")
	if movie2 == "" :
		print(movie)
	else:
		print(movie2)
fav_movie()


# Task 2

def calculator():

	'''Calculator function will use 2 number inputs and perform addition, subtraction, multiplication, division.

	variables:
	num1 -> first input float number
	num2 -> second input float number
	'''
	num1 = float(input("Enter first number: "))
	num2 = float(input("Enter second number: "))
	def addition():
		'''Performs addition on num1, num2 and prints the result'''
		print("The sum is: " + str(num1 + num2))
	addition()
	def subtraction():
		'''Performs subtraction on num1, num2 and prints the result'''
		print("The difference is " + str(num1 - num2))
	subtraction()
	def product():
	    '''Performs multiplication on num1, num2 and prints the result'''
	    print("The product is: " + str(num1 * num2))
	product()
	def div():
	    '''Performs division on num1, num2 and prints the result'''
	    print("The division result is: " + str(num1 / num2))
	div()        	
calculator()


# Task 3

'''Displays a user input string 20 times.
   Prints in seperate lines for neatness.

   variable:
   string -> to store user input string
'''   

def repeater():
	string = input("Enter any string: ") + "\n"
	print(string * 20)
repeater()


# Task 4

def sentence():
	
	'''Displays list of words seperated by comma in a user input sentence.
	   Prompts user for entering a word to perform word count on the sentence.

	   variables:
	   com -> list used to include words seperated by commas
	   word -> to store word to be used for word count
	'''
	   
	sent = input("Enter a complete sentence: ")
	com = []
	com.append(sent.split(','))
	print("Words seperated by commas are: ", *com)

	word = input("Enter word for word count: ")
	print(sent.count(word))
sentence()


# Task 5

def replace():

	'''Removes certain number of characters from end of string.
	   Number of characters and string to be provided by user.

	   variables:
	   string2 -> user input string
	   char -> integer variable. Number of characters to be removed
	   temp -> stores number of characters to be printed
	'''
	   
	string2 = input("Enter a string: ")
	char = int(input("Enter number of characters to be removed from string's end: "))
	temp = len(string2) - char
	print(string2[0:temp])
replace()