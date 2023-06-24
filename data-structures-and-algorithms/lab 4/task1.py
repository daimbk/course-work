# Daim Bin Khalid
# 251686775
# Lab 5

# Task 1
# Given the array of integers a and an integer n, verify whether n appears in a. Also compute time complexity.
# Time Complexity: O(n)
def check_in_array(a, n):
    if len(a) == 0:
        return False
    elif n == a[0]:
        return True
    else:
        return check_in_array(a[1:], n)


print(check_in_array([3, 4, 5, 6], 4))
