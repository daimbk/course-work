# Lab 2
# Name : Daim Bin Khalid
# Roll no : 251686775

# Question 1

def wc():

	line_count = 0 
	word_count = 0 
	char_count = 0

	filename = input('Enter file name: ')
	infile = open(filename + '.txt')
	line = infile.readline()

	while line != '':
		line_count += 1
		word_count += len(line.split())
		char_count += len(line)
		line = infile.readline()
	print('There are', line_count, 'lines,', word_count, 'words, and', char_count, 'characters.')
	
wc()


# Question 2, 3, 4 environment diagrams attached in zip file