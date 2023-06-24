# Daim Bin Khalid
# 251686775
# Lab 5

# Task 2
# Given an array of integers a and an integer n, returns the number of occurrences of n in a. Also compute time complexity
# Time Complexity: O(n)
def occurrences(a, n):
    counter = 0
    if len(a) == 0:
        return counter
    elif n == a[0]:
        counter += 1
        return counter + occurrences(a[1:], n)
    else:
        return counter + occurrences(a[1:], n)


print(occurrences([9, 8, 7, 9, 2, 9], 3))
