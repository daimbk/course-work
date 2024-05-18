import time
from multiprocessing import Process, current_process
from math import floor


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quicksort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)

        process_name = current_process().name
        if process_name == 'main':
            leftArm = Process(target=quicksort, args=(array, low, pivot - 1))
            rightArm = Process(target=quicksort, args=(array, pivot + 1, high))
            leftArm.start()
            rightArm.start()
            leftArm.join()
            rightArm.join()
        else:
            quicksort(array, low, pivot - 1)
            quicksort(array, pivot + 1, high)


def find_median(num_list, size):
    if size % 2 == 0:
        return floor((num_list[size // 2 - 1] + num_list[size // 2]) / 2)
    else:
        return floor(num_list[size // 2])


if __name__ == '__main__':
    numbers = [90, 8, 80, 30, 72, 49, 79, 56, 39, 42, 93, 10, 23, 78, 7, 98, 10, 80, 26, 95, 34, 96, 83, 13, 57, 50, 49, 32, 82,
               55, 69, 71, 10, 50, 31, 4, 89, 49, 99, 36, 46, 65, 46, 72, 33, 73, 49, 100, 23, 9]

    start_time = time.time()

    size = len(numbers)
    quicksort(numbers, 0, size - 1)
    median = find_median(numbers, size)
    print(f'Median: {median}')

    end_time = time.time()
    print(f'Execution time: {end_time - start_time}s')
