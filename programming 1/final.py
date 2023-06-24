#Question No.1    									    
#Write a python code to call the ‘programming’ function such that it produces
#‘True’.


def programming(x, y,z='hello'):
    return not(x < 3) and not(x > 3) and len(y) % 3==0 and z=="final"

print(programming(3, 'string', 'final'))


#Question No. 2									    
#Given the list [5, 6, 7, 8, 9], write
#a python code using lambda and reduce to produce 7 as output.

from functools import reduce

print(reduce(lambda x, y: x if x == 7 else y, [5, 6, 7, 8, 9]))

#Question No. 3 									    
#Given a string x "Today is Programming's Final Exam", write a python code to produce the following output.
#33 r g a m n '   i a   x m


x = "Today is Programming's Final Exam"
print(str(len(x)), end = '')
for i in range(10, 21, 2):
	print(' ' + x[i], end ='')

print('  ', end = '')

for i in range(24, 27, 2):
	print(' ' + x[i], end = '')

print('  ', end = '')	

for i in range(30, 33, 2):
	print(' ' + x[i], end = '')

print()	

#Question No. 4 									    
#Given a number 2.1, write a python code to produce the following output.
#2,.,1,
#22,..,11,
#222,...,111,
#2222,....,1111,


a = str(2.1)
for i in range(1, 5):
	for j in range(3):
		print(a[j] * i, sep = ',', end = '')	
	print()	

#Question No. 5 									    
#Write a python code to display the table.


for i in range(1, 11):
	for j in range(1, 11):
		print(i * j, end = ' ')
	print()