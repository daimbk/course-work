'''
Part A: Design an algorithm to add 3 (+3 units) in all even numbers and to add 2 (+2 units) 
in all odd indices in the first 1/5th elements of the given n integer list.


1. Brute Force Approach

void addIndices(Temp[1..n], size) {
    one_fifth = floor(size / 5)

    for i: 1..n
        if (Temp[i] % 2 == 0)
            Temp[i] += 3

            if (i <= one_fifth AND i & 2 != 0)
                Temp[i] += 2
}


2. Divide & Conquer
Recurrence Relation: T(n) = 2T(n/2) + 1

void addIndices(Temp[1..n], start, end, size) {
    if (start == end AND Temp[start] % 2 == 0)
        Temp[start] += 3

        if ((start == end) AND (start % 2 != 0) AND (start < size / 5))
            Temp[start] += 2

        return

    mid = floor((start + end) / 2)
    addIndices(Temp[1..n], start, mid, size)
    addIndices(Temp[1..n], mid + 1, end, size)
}
'''

from math import floor


def addIndices(tempList, size):
    """Brute force"""
    one_fifth = floor(size / 5)

    for i in range(size):
        if (tempList[i] % 2 == 0):
            tempList[i] += 3

            if ((i <= one_fifth) and (i % 2 != 0)):
                tempList[i] += 2


# Divide & Conquer
def addIndicesDC(tempList, start, end, size):
    if (start == end and tempList[start] % 2 == 0):
        tempList[start] += 3

        if ((start == end) and (start % 2 != 0) and (start < size / 5)):
            tempList[start] += 2

        return

    mid = floor((start + end) / 2) + 1
    addIndicesDC(tempList, start, mid, size)
    addIndicesDC(tempList, mid + 1, end, size)


# test
tempList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
size = len(tempList)

# Brute Force Approach
# addIndices(tempList, size)
# print("Brute Force Result:", tempList)

# Reset the tempList
# tempList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Divide & Conquer Approach
addIndicesDC(tempList, 0, 9, size)
print("Divide & Conquer Result:", tempList)
