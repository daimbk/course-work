'''
Part C: Consider a sorted list which is sorted in ascending-order. This list can only have 
multiple occurrences of A’s, B’s and C’s.  Design an algorithm to count the total number of 
B’s in this sorted list. Make it intelligent by using its sorted order. Note: It is possible that 
the list has only A’s or only B’s or only C’s. It is also possible that list have no A’s or no B’s or 
no C’s.


1. Brute Force

returnValue countB(Temp[1...n]) {
    sum = 0

    for i: 1...n
        if (Temp[i] == "B")
            sum += 1

    return sum
}


2. Divide & Conquer
Recurrence Relation: T(n) = 2T(n/2) + 1

returnValue countB(Temp[1...n], start, end) {
    if (start == end AND Temp[start] == "B")
        return 1
    elseif (start == end AND Temp[start] != "B")
        return 0

    if (Temp[start] == "B" AND Temp[end] == "B")
        return end - start + 1

    if (Temp[end] == "A")
        return 0

    if (Temp[start] == "C")
        return 0

    mid = floor((start + end) / 2)
    leftCount <-- countB(Temp[1...n], start, mid)
    rightCount <-- countB(Temp[1...n], mid + 1, end)

    return leftCount + rightCount
}
'''


def countB(tempList):
    # Brute Force
    sum = 0

    for i in tempList:
        if (i == "B"):
            sum += 1

    return sum


def countB_DC(tempList, start, end):
    # Divide & Conquer
    if (start == end and tempList[start] == "B"):
        return 1

    elif (start == end and tempList[start] != "B"):
        return 0

    if (tempList[start] == "B" and tempList[end] == "B"):
        return end - start + 1

    if (tempList[end] == "A"):
        return 0

    if (tempList[start] == "C"):
        return 0

    mid = (start + end) // 2
    leftCount = countB_DC(tempList, start, mid)
    rightCount = countB_DC(tempList, mid + 1, end)

    return leftCount + rightCount


# test
tempList = ["A", "B", "B", "B", "C", "C", "C", "C", "C", "C"]

# Brute Force Approach
size = countB(tempList)
print("Brute Force Result:", size)

# Reset the tempList
tempList = ["A", "B", "B", "B", "C", "C", "C", "C", "C", "C"]

# Divide & Conquer Approach
size = countB_DC(tempList, 0, 9)
print("Divide & Conquer Result:", size)
