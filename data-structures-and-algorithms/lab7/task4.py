class Empty(Exception):
    pass


class CircularQueue:
    '''
    FIFO queue implementation using a Python list as underlying storage.
    '''
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self):
        self._data = [None] * CircularQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        '''
        Return the number of elements in the queue.
        '''
        return self._size

    def is_empty(self):
        '''
        Return True if the queue is empty.
        '''
        return self._size == 0

    def first(self):
        '''
        Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        '''
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def dequeue(self):
        '''
        Remove and return the ﬁrst element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        '''
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        '''
        Add an element to the back of queue.
        '''
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):  # we assume cap >= len(self)
        '''
        Resize to a new list of capacity >= len(self).
        '''
        old = self._data  # keep track of existing list
        self._data = [None] * cap  # allocate list with new capacity
        walk = self._front
        for k in range(self._size):  # only consider existing elements
            self._data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self._front = 0  # front has been realigned


class Process:
    def __init__(self):
        self.q = CircularQueue()

    def addTask(self, name, time):
        self.data = [name, time]
        self.q.enqueue(self.data)
        print()
        print(self.data[0], " is added for ", self.data[1], " minutes.")

    def deleteTask(self):
        if not self.q.is_empty():
            a = self.q.dequeue()
            print(a, " is deleted.")
            return a

    def scheduler(self):
        while not self.q.is_empty():
            print()
            task = self.q.dequeue()
            print(f'{task[0]} is running for {task[1]} minutes')
            task[1] = task[1] - 10
            if task[1] > 0:
                self.q.enqueue(task)
                print(f'{task[0]} again added to queue for {task[1]} minutes')
                print()
            else:
                print(task[0], " is done.")
                print()
            for i in self.q._data:
                if i:
                    print(i, end=" ")
            print()


n = 0
proc = Process()
while n == 0:
    print("\n1. Add Task\n2. Delete Task\n3. Run Scheduler\n4. Exit\n")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        name = input("Enter task name : ")
        time = int(input("Enter task time : "))
        proc.addTask(name, time)
    elif choice == 2:
        if not proc.q.is_empty():
            (proc.deleteTask())
        else:
            print("Empty Queue")
    elif choice == 3:
        proc.scheduler()
    elif choice == 4:
        n = 1
    else:
        print("Invalid Key!!")
