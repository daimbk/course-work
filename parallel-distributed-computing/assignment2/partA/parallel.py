import time
import multiprocessing


def checkSector(line):
    point = line.strip().split(',')
    x, y = int(point[0]), int(point[1])

    if (x == 0 and y == 0) or (x > 0 and y > 0 and x <= y):
        return "A"

    elif x > 0 and y >= 0 and x > y:
        return "B"

    elif x > 0 and y < 0 and x >= abs(y):
        return "C"

    elif x >= 0 and y < 0 and abs(y) > x:
        return "D"

    elif x < 0 and y < 0 and x >= y:
        return "E"

    elif x < 0 and y <= 0 and y > x:
        return "F"

    elif x < 0 and y > 0 and abs(x) >= y:
        return "G"

    elif x <= 0 and y > 0 and y > abs(x):
        return "H"


def count_points():
    sectors = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0}
    chunk_size = 10000

    with open("coordinate_points.txt", "r") as p_file:
        # read file in chunks
        with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
            sector_counters = pool.map(checkSector, p_file, chunk_size)

        # store sector count
        for sector in sector_counters:
            sectors[sector] += 1

    print(f'A: {sectors["A"]}\nB: {sectors["B"]}\nC: {sectors["C"]}\nD: {sectors["D"]}\nE: {sectors["E"]}\nF: {sectors["F"]}\nG: {sectors["G"]}\nH: {sectors["H"]}')
    total_points = sum(sectors.values())
    print(f'Total: {total_points}')


if __name__ == '__main__':
    start_time = time.time()
    count_points()
    end_time = time.time()
    print(f'Execution time: {end_time - start_time}s')
