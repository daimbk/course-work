# Lab 3
# Name : Daim Bin Khalid
# Roll no : 251686775

# Question 1

def probability(n, k):
	if k == 1:
		return n
	elif n < k:
		return 0
	else:
		return probability(n - 1, k - 1) + probability(n - 1, k)

print(probability(6, 2))


# Question 2

num_list = [42, 1, 78, 89, 999, 420, 69, 765]

def maximum(numlist, lowest, highest):
	if lowest == highest:
		return numlist[lowest]
	else:
		greatest = maximum(numlist, lowest + 1, highest)
		if numlist[lowest] >= greatest:
			return numlist[lowest]
		else:
			return greatest

print(maximum(num_list, 0, 7))