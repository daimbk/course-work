from queue import Empty
from random import randint


class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()


def main():
    stack = Stack()
    for i in range(25):
        stack.push(randint(0, 100))

    for i in range(12):
        stack.top()

    for i in range(10):
        stack.pop()

    print(f'Size of stack is: {stack.__len__()}')


main()
