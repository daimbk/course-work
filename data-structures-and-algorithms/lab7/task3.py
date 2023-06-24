from queue import Empty


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

    def get_stack(self):
        return self._data

    def print_stack(self):
        print(self._data)


# Write a python program that reverses a string using stack.
def main():
    stack = Stack()

    string_input = input("Enter a string: ")
    string_list = [i for i in string_input]

    for i in string_list:
        stack.push(i)

    reverse_string = ''
    for i in range(len(string_list)):
        reverse_string += stack.pop()

    print(reverse_string)


main()
