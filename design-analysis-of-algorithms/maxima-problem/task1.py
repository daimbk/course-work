'''
Task 1: Design an algorithm for the maxima point problem (as discussed in class)
for a point in 3-D space i.e. a point having its x, y & z components.
'''

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # Into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i].x <= R[j].x:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def maxima_points(points_list):
    stack = Stack()

    for point in points_list:
        while not stack.is_empty() and stack.peek().y <= point.y and stack.peek().z <= point.z:
            stack.pop()

        stack.push(point)

    return stack
