'''
Task 6: Design geometric approach for minima-point problem while sweeping
the sweep line along y-direction?
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
            if L[i].y <= R[j].y:
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


def minima_points(points_list):
    stack = Stack()

    for point in points_list:
        while not stack.is_empty() and stack.peek().x >= point.x and stack.peek().z >= point.z:
            stack.pop()

        stack.push(point)

    return stack


def main():
    n = int(input("Enter the number of points: "))
    points = []

    for _ in range(n):
        x, y, z = map(int, input("Enter the point: ").split())
        points.append(Point(x, y, z))

    mergeSort(points)
    print("\nSorted points")
    for point in points:
        print(point.x, point.y, point.z)

    minima = minima_points(points)

    print("\nMinima Points:")
    for point in minima.items:
        print(point.x, point.y, point.z)


if __name__ == "__main__":
    main()
