'''
Task 2: Write python/C++/Java script for your above algorithm and generate
screen dump of your program's output for at least 7 points. Note that your program should
be general and should work fine for any value of n points.
'''

import task1


def main():
    n = int(input("Enter the number of points: "))
    points = []

    for _ in range(n):
        x, y, z = map(int, input("Enter the point: ").split())
        points.append(task1.Point(x, y, z))

    task1.mergeSort(points)
    print("\nSorted points")
    for point in points:
        print(point.x, point.y, point.z)

    maxima = task1.maxima_points(points)

    print("\nMaxima Points:")
    for point in maxima.items:
        print(point.x, point.y, point.z)


if __name__ == "__main__":
    main()
