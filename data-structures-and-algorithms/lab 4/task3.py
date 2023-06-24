# Daim Bin Khalid
# 251686775
# Lab 5

# Task 3
"""Given an array of integers a, returns a new array obtained from a by replacing each negative integer with 0. Also compute time complexity.
For example, the call negativesToZero({1,-2, 3, 4, -5}), should return the array {1, 0, 3, 4, 0}"""

# Time Complexity: O(n)


def negative_to_positive(a, new_list):
    if len(a) == 0:
        return new_list
    elif a[0] < 0:
        new_list.append(0)
        return negative_to_positive(a[1:], new_list)
    else:
        new_list.append(a[0])
        return negative_to_positive(a[1:], new_list)


pos_list = []
print(negative_to_positive([-9, -8, 7, 6, 5, -4, 7, 3], pos_list))
