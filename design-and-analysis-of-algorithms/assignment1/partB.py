'''
Part B: Design an algorithm to take sum of ‘n’ integers given that we want our linear 
structure (list/array) to be divided into three parts instead of two parts at each recursive 
step. You need to change the base condition(s) carefully.


1. Brute Force

returnValue sumArr(Temp[1...n]) {
    sum = 0

    for i: 1...n
        sum += Temp[i]

    return sum
}


2. Divide & Conquer
Recurrence Relation: T(n) = 3T(n/3) + 1

returnValue sumArr(Temp[1...n], start, end) {
    if (start == end)
        return Temp[start]
    elseif (start == end - 1)
        return Temp[start] + Temp[end]
    elseif (start == end - 2)
        return Temp[start] + Temp[start + 1] + Temp[end]


    div1 = floor((start + end) / 3)
    div2 = floor(div1 * 2)

    leftSum <- sumArr(Temp[1...n], start, div1)
    midSum <- sumArr(Temp[1...n], div1 + 1, div2)
    rightSum <- sumArr(Temp[1...n], div2 + 1, end)

    return leftSum + midSum + rightSum
}
'''

from math import floor


def sumArr(list):
    # Brute Force
    sum = 0

    for i in list:
        sum += i

    return sum


def sumArrDC(tempList, start, end):
    # Divide & Conquer
    if (start == end):
        return tempList[start]

    elif (start == end - 1):
        return tempList[start] + tempList[end]

    elif (start == end - 2):
        return tempList[start] + tempList[start + 1] + tempList[end]

    div1 = floor((start + end) / 3)
    div2 = floor(div1 * 2)

    leftSum = sumArrDC(tempList, start, div1)
    midSum = sumArrDC(tempList, div1 + 1, div2)
    rightSum = sumArrDC(tempList, div2 + 1, end)

    return leftSum + midSum + rightSum
