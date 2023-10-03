'''
Part E: Consider that you have two arrays of positive integers T and Z. Write a program 
that compares the content of the two arrays and returns ‘true’ if the content of both arrays 
is the same and return ‘false’ otherwise.


1. Brute Force

bool compare(T[1..n], Z[1..n]) {
    for i: 1..n
        if (T[i] != Z[i])
            return false

    return true
}


2. Divide & Conquer
Recurrence Relation: T(n) = 2T(n/2) + 1

bool compare(T[1..n], Z[1..n], start, end) {
    if (start == end)
        if (T[start] == Z[start])
            return true
        else
            return false

    mid = floor((start + end) / 2)
    leftCheck <-- compare(T[1..n], Z[1..n], start, mid)
    rightCheck <-- compare(T[1..n], Z[1..n], mid + 1, end)

    return leftCheck AND rightCheck
}
'''


def compare(T, Z, size):
    # Brute Force
    for i in range(size):
        if (T[i] != Z[i]):
            return False

    return True


def compareDC(T, Z, start, end):
    # Divide & Conquer
    if (start == end):
        if (T[start] == Z[start]):
            return True
        else:
            return False

    mid = (start + end) // 2
    leftCheck = compareDC(T, Z, start, mid)
    rightCheck = compareDC(T, Z, mid + 1, end)

    return leftCheck and rightCheck


# test
tempList1 = [1, 2, 3, 4]
tempList2 = [1, 2, 3, 4]

# Brute Force Approach
flag = compare(tempList1, tempList2, 4)
print("Brute Force Result:", flag)

# Reset the tempList
tempList1 = [1, 2, 3, 4]
tempList2 = [1, 2, 3, 4]

# Divide & Conquer Approach
flag = compareDC(tempList1, tempList2, 0, 3)
print("Divide & Conquer Result:", flag)
