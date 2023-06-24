# Lab1.
# Name: Daim Bin Khalid
# Roll no: 251686775


# Q1

invest = 10
final = invest
years = 0

while (final <= (2 * invest)):
	final += 0.05 * final
	years += 1

print(years, 'years were taken to double.')


# Q2

from math import sqrt

n = int(input('Enter a number "n": '))

for i in range(2, n + 1):
	if i > sqrt(n) and n % i == 0:
		print('Not prime, ', i, 'evenly divides it.')
		break
	elif i <= sqrt(n) and n % i != 0:
		print('Number is prime')
		break


# Q3

mystery = {'Daim' : 21, 'Manal-ud-deen' : 68, 'Momi' : 0, 'Hafsah' : 90, 'Kiran' : 20}

def ageing(dict):
	for i in dict:
		dict[i] += 1
	return dict

print(ageing(mystery))


# Q4

studid = input('Enter student id: ')
infile = open('classes.txt', 'r')
line = infile.readline().rstrip('\n')

while line != '':
    subfile = line + '.txt'
    report = open(subfile, 'r')
    grade = report.readline().split()
    
    while len(grade) != 0:
        if studid == grade[0]:
            print(line, '\t', grade[1])
        grade = report.readline().split()
    line = infile.readline().rstrip('\n')