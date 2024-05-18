import time
from multiprocessing import Process, current_process, Manager
from math import floor


def median_of_medians(arr):
    sub_lists = [arr[j: j + 5] for j in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sub_lists]

    if len(medians) <= 5:
        return sorted(medians)[len(medians) // 2]
    else:
        return median_of_medians(medians)


def partition(array, low, high):
    pivot = median_of_medians(array[low:high+1])
    pivot_index = array.index(pivot)
    array[pivot_index], array[high] = array[high], array[pivot_index]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quicksort(array, low, high, shared_array):
    if low < high:
        pivot = partition(array, low, high)
        shared_array[low:high+1] = array[low:high+1]

        process_name = current_process().name
        if process_name == 'main':
            leftArm = Process(target=quicksort, args=(
                array, low, pivot - 1, shared_array))
            rightArm = Process(target=quicksort, args=(
                array, pivot + 1, high, shared_array))
            leftArm.start()
            rightArm.start()
            leftArm.join()
            rightArm.join()
        else:
            quicksort(array, low, pivot - 1, shared_array)
            quicksort(array, pivot + 1, high, shared_array)


def find_median(num_list, size):
    if size % 2 == 0:
        return floor((num_list[size // 2 - 1] + num_list[size // 2]) / 2)
    else:
        return floor(num_list[size // 2])


if __name__ == '__main__':
    numbers = [90, 8, 80, 30, 72, 49, 79, 56, 39, 42, 93, 10, 23, 78, 7, 98, 10, 80, 26, 95, 34, 96, 83, 13, 57, 50, 49, 32, 82,
               55, 69, 71, 10, 50, 31, 4, 89, 49, 99, 36, 46, 65, 46, 72, 33, 73, 49, 100, 23, 9]

    start_time = time.time()

    manager = Manager()
    shared_array = manager.list(numbers)

    size = len(numbers)
    quicksort(numbers, 0, size - 1, shared_array)
    sorted_numbers = list(shared_array)
    median = find_median(sorted_numbers, size)
    print(f'Median: {median}')

    end_time = time.time()
    print(f'Execution time: {end_time - start_time}s')
