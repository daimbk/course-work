'''
Part D: Consider that you will be given a list of size in powers of 2. (e.g. 2,4,8,16 ... etc.) You 
have to swap the consecutive elements in such a way that first element should be swapped 
with its immediate neighbor element and so on.


1. Brute Force

void swap(Temp[1..n]) {
    for i: 1..n (i += 2)
        temp <-- Temp[i]
        Temp[i] = Temp[i + 1]
        Temp[i + 1] = temp
}


2. Divide & Conquer
Recurrence Relation: T(n) = 2T(n/2) + 1

void swap(Temp[1..n], start, end) {
    if (start == end - 1)
        temp = Temp[start]
        Temp[start] = Temp[end]
        Temp[end] = temp

        return

    else
        mid = floor((start + end) / 2)
        swap(Temp[1..n], start, mid)
        swap(Temp[1..n], mid + 1, end)
}
'''


def swap(tempList, size):
    # Brute Force
    for i in range(0, size, 2):
        temp = tempList[i]
        tempList[i] = tempList[i + 1]
        tempList[i + 1] = temp


def swapDC(tempList, start, end):
    # Divide & Conquer
    if (start == end - 1):
        temp = tempList[start]
        tempList[start] = tempList[end]
        tempList[end] = temp

        return

    else:
        mid = (start + end) // 2
        swapDC(tempList, start, mid)
        swapDC(tempList, mid + 1, end)


# test
tempList = [2, 4, 8, 16]

# Brute Force Approach
swap(tempList, 4)
print("Brute Force Result:", tempList)

# Reset the tempList
tempList = [2, 4, 8, 16]

# Divide & Conquer Approach
swapDC(tempList, 0, 3)
print("Divide & Conquer Result:", tempList)
