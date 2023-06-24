# Lab 4 
# Daim Bin Khalid
# 251686775

# Question 1

from math import pi

class sphere:

	def __init__(self, radius):
		self.radius = radius

	def getRadius(self):
		return self.radius

	def surfaceArea(self):
		self.area = (4 * pi * self.radius ** 2)
		return self.area

	def volume(self):
		self.volume = (4/3) * pi * (self.radius ** 3)
		return self.volume
	

# Question 2

class playing_card:

	def __init__(self, rank, suit):
		if (rank > 0 and rank < 14) and (suit == 'd' or suit == 'c' or suit == 'h' or suit == 's'):
			self.rank = rank

		if suit == 'd':
			self.suit = 'Diamonds'
		elif suit == 'c':
			self.suit = 'Clubs'
		elif suit == 'h':
			self.suit = 'Hearts'
		elif suit == 's':
			self.suit = 'Spades'			

	def getRank(self):
		return self.rank 

	def getSuit(self):
		return self.suit 

	def BJValue(self):
		if self.rank > 10:
			return 10
		else:
			return self.rank

	def __str__(self):
		if self.rank == 1:
			return ('Ace of ' + self.suit)
		elif self.rank == 11:
			return ('Jack of ' + self.suit)
		elif self.rank == 12:
			return ('Queen of ' + self.suit)
		elif self.rank == 13:
			return ('King of ' + self.suit)
		elif self.rank > 1 and self.rank < 11:
			return (str(self.rank) + ' of ' + self.suit)


# Question 3

class Customer:

	def __init__(self, cid, balance, acid):
		self.CustomerID = cid 
		self.CurrentBalance = balance
		self.AccountID = acid

	def DisplayInfo(self):
		print(self.CustomerID)
		print(self.CurrentBalance)
		print(self.AccountID)

def main():

	# Question 1
	newsphere = sphere(5)

	# Question 2
	import random
	suits_list = ['c', 'h', 's', 'd']

	n = int(input('Enter the number of random cards to generate: '))
	
	for i in range(n):
		rank = random.randrange(1, 13)
		suit = random.choice(suits_list)
		card = playing_card(rank, suit)
		print(card)

	#Question 3
	daim = Customer('Daim', 4500, 2310)
	daim.DisplayInfo()

main()