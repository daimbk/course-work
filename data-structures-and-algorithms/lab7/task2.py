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

    def print_stack(self):
        print(self._data)


# Write a python program that checks brackets are balanced in an expression using stack
def main():
    stack = Stack()

    loop = False
    while not loop:
        bracket_input = input("Enter opening brackets or N to stop: ")
        if bracket_input == "N":
            loop = True
        elif bracket_input == "(" or "[" or "{":
            stack.push(bracket_input)

    stack.print_stack()

    while stack.__len__() != 0:
        closing_bracket = input("Enter closing bracket: ")
        if closing_bracket == ")" and stack.top() == "(":
            stack.pop()
        elif closing_bracket == "]" and stack.top() == "[":
            stack.pop()
        elif closing_bracket == "}" and stack.top() == "{":
            stack.pop()
        else:
            print("Wrong bracket or input")

    print(f'Stack length: {stack.__len__()}')


main()
