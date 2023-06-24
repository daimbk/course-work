# Daim Bin Khalid
# Roll no.: 251686775
# Lab 12: Heap

class HeapPriorityQueue:
    def __init__(self, array):
        self.heap = array

    def enqueue(self, key, value):
        self.heap.append((key, value))

        last_element = len(self.heap) - 1
        self.up_heap(last_element)

    def up_heap(self, index):

        while index > 0 and self.heap[index][0] < self.heap[self.get_parent(index)[0]]:
            self.swap(index, self.heap.index(self.get_parent(index)))
            index = self.get_parent(index)

    def dequeue(self):
        self.swap(0, -1)

        self.heap.pop()
        self.down_heap(0)

    def down_heap(self, index):

        while self.has_child(index):
            min_child = self.minimum_child(index)

            if self.heap[index][0] < min_child[0]:
                break

            self.swap(index, self.heap.index(min_child))
            index = self.heap.index(min_child)

    def minimum_child(self, index):
        if not self.get_right(index):
            return self.get_left(index)[0]
        else:
            left_child = self.get_left(index)
            right_child = self.get_right(index)
            if left_child[0] > right_child[0]:
                return right_child
            else:
                return left_child

    def has_child(self, index):
        if self.get_left:
            return True
        else:
            return False

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def min(self):
        return self.heap[0][1]

    def get_left(self, index):
        return self.heap[2 * index + 1]

    def get_right(self, index):
        return self.heap[2 * index + 2]

    def get_parent(self, index):
        return self.heap[(index - 1) // 2]

    def __len__(self):
        return len(self.heap)


# question 3
def heap_sort(queue):
    heap = HeapPriorityQueue(queue)
    sorted_array = []
    while heap.heap:
        sorted_array.append(heap.dequeue())
    return sorted_array
