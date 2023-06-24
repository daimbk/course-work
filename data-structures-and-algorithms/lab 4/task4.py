# Daim Bin Khalid
# 251686775
# Lab 5

# Task 4
""" Given an array of integers a, inverts the positions of its elements. Also compute time complexity.
For example, the call invert(a), where a is a reference to the array {1, 2, 3, 4}, should
modify the array in such a way that a refers to {4, 3, 2, 1}."""

# Time Complexity: O(n)


def invert_list(a):
    if len(a) == 0:
        return []
    return [a[-1]] + invert_list(a[:-1])


print(invert_list([1, 2, 3, 4]))
