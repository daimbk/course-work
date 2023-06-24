# Lab 6
# Daim Bin Khalid
# 251686775

class Actor:

	common_list = []

	def __init__(self):
		self.movielist = []

	def setName(self, split):
		self.name = split[0].lstrip()

	def setDOB(self, split):
		self.dob = split[1].lstrip()

	def setGender(self, split):
		self.gender = split[2].lstrip()
		self.gender = self.gender.rstrip('\n')

	def getName(self):
		return self.name

	def getDOB(self):
		return self.dob

	def getGender(self):
		return self.gender

	def AddMovie(self, movie):
		self.movielist.append(movie)

	def getMovies(self):
		return self.movielist	

	def DisplayActor(self):
		print('Name: ' + self.name)
		print('Date of Birth: ' + self.dob)
		print('Gender: ' + self.gender)
		print('Movies starred in: ', end = '') 
		print(*self.movielist, sep = ', ')	

	def CompareActor(self, other):
		for i in self.movielist:
			if i in other.movielist:
				Actor.common_list.append(i)
		return Actor.common_list

def main():

	actor_list = []

	infile = open('actor.txt', 'r')
	for line in infile:
		split = line.split(',')
		actor = Actor()
		actor_list.append(actor)
		actor.setName(split)
		actor.setDOB(split)
		actor.setGender(split)

	actor_list[0].AddMovie('Tenet')
	actor_list[0].AddMovie('Interstellar')
	actor_list[1].AddMovie('123')
	actor_list[1].AddMovie('Tenet')

	for i in actor_list:
		i.DisplayActor()
		print()

	print('Common movies are: ', end = '')
	print(actor_list[0].CompareActor(actor_list[1]))

main()