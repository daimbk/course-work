# Assignment 1
# Daim Bin Khalid
# 251686775

# Problem 1

def alphanum(number):
	engnum = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

	if number >= 0 and number < 10:
		return engnum[number]
	else:
		return alphanum(number // 10) + ' ' + engnum[number % 10]

print('Problem 1:')
print(alphanum(int(input('Enter number to convert to alphabetical: '))))


# Problem 2

class die:
    roll_result = 0

    def __init__(self):
        self.faces = [1, 2, 3, 4, 5, 6]

    def roll(self):
        import random
        die.roll_result = random.choice(self.faces)
        return die.roll_result

    def showFace(self):
        print(die.roll_result)


class statistics:
    def __init__(self):
        self.data_set = []
        self.sum = 0
        self.total = 0

    def enter(self, item):
        self.data_set.append(item)

    def getSum(self):
        for i in self.data_set:
            self.sum += i
        return self.sum

    def getMean(self):
        self.mean = self.sum / len(self.data_set)
        return self.mean

    def getStdDev(self):
        def variance(data, ddof = 0):
            for i in self.data_set:
                self.total += (i - self.mean) ** 2
            return self.total / (len(self.data_set) - ddof)

        def stdev(data):
            var = variance(self.data_set)
            return var ** (1 / 2)

        return stdev(self.data_set)      

    def Max(self):
    	highest = 0
    	for i in self.data_set:
    		if i > highest:
    			highest = i 
    	return highest
    	
    def Min(self):
    	lowest = 1000000000
    	for i in self.data_set:
    		if i < lowest:
    			lowest = i
    	return lowest		  


def main():
    match = die()
    new_stats = statistics()

    print('\nProblem 2:')

    face_check = int(input('Enter which die face (1-6) to get stats for: '))
    exp_num = int(input('Enter how many times the experiment will be done (each experiment has 50 die rolls): '))

    for i in range(exp_num):
    	count = 0
    	for i in range(50):
    		newface = match.roll()
    		if newface == face_check:
    			count += 1
    	new_stats.enter(count)

    outfile = open('statsresult.txt', 'w')
    outfile.write('The statistics for die face ' + str(face_check) + ' after ' + str(exp_num) + ' experiments are:\n')    
    outfile.write('Sum :' + str(new_stats.getSum()) + '\n')
    outfile.write('Minimum :' + str(new_stats.Min()) + '\n')
    outfile.write('Maximum :' + str(new_stats.Max()) + '\n')
    outfile.write('Mean :' + str(new_stats.getMean()) + '\n')
    outfile.write('Standard Deviation :' + str(new_stats.getStdDev()) + '\n')
    outfile.close()
    print('Output saved in filename "statsresult"')
main()