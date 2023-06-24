# Lab 3
# Daim Bin Khalid
# 251686775

import random
from time import time

start_time = time()  # record the starting time


def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = []
for i in range(100000):
    array.append(random.randint(1, 100000))

element = 68750

result = binarySearch(array, element, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")


end_time = time()  # record the ending time
elapsed = end_time - start_time  # compute the elapsed time

print('Start time: ', start_time)
print('End time: ', end_time)
print('Time Taken: ', elapsed)
