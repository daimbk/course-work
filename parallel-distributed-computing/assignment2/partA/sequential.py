import time


def count_points(points_file):
    sectors = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0}

    with open(points_file, "r") as p_file:
        for point in p_file:
            point = point.strip().split(',')
            x, y = int(point[0]), int(point[1])

            # A: x > 0, y > 0, x <= y, (x = 0, y = 0, origin points in A)
            # B: x > 0, y >= 0, x > y
            # C: x > 0, y < 0, x >= y(abs)
            # D: x >= 0, y < 0, y(abs) > x
            # E: x < 0, y < 0, x >= y
            # F: x < 0, y <= 0, y > x
            # G: x < 0, y > 0, x(abs) >= y
            # H: x <= 0, y > 0, y > x(abs)

            if (x == 0 and y == 0) or (x > 0 and y > 0 and x <= y):
                sectors["A"] += 1

            elif x > 0 and y >= 0 and x > y:
                sectors["B"] += 1

            elif x > 0 and y < 0 and x >= abs(y):
                sectors['C'] += 1

            elif x >= 0 and y < 0 and abs(y) > x:
                sectors["D"] += 1

            elif x < 0 and y < 0 and x >= y:
                sectors["E"] += 1

            elif x < 0 and y <= 0 and y > x:
                sectors["F"] += 1

            elif x < 0 and y > 0 and abs(x) >= y:
                sectors["G"] += 1

            elif x <= 0 and y > 0 and y > abs(x):
                sectors["H"] += 1

    print(f'A: {sectors["A"]}\nB: {sectors["B"]}\nC: {sectors["C"]}\nD: {sectors["D"]}\nE: {sectors["E"]}\nF: {sectors["F"]}\nG: {sectors["G"]}\nH: {sectors["H"]}')
    total_points = sum(sectors.values())
    print(f'Total: {total_points}')


if __name__ == '__main__':
    start_time = time.time()
    count_points("coordinate_points.txt")
    end_time = time.time()
    print(f'Execution time: {end_time - start_time}s')
