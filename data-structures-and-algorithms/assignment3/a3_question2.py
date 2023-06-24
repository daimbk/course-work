# Assignment 3: Binary Search Trees
# Name: Daim Bin Khalid
# Roll no.: 251686775
# Question 2: Expression Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ExpTree:
    def __init__(self):
        self.operands = ["+", "-", "/", "*"]
        self.stack = []

    def parsePostfix(self, expression):
        expression = list(expression)

        for value in expression:
            if value not in self.operands and value != " ":
                node = Node(value)
                self.stack.append(node)
            elif value != " ":
                operand_node = Node(value)
                operand_node.right = self.stack.pop()
                operand_node.left = self.stack.pop()
                self.stack.append(operand_node)

    def in_order(self, node, expression_string):
        if node == None:
            return expression_string
        else:
            if node.value in self.operands:
                expression_string += "(" + self.in_order(node.left, expression_string) + \
                    node.value + \
                    self.in_order(node.right, expression_string) + ")"
            else:
                expression_string += node.value
            return expression_string

    def toInFix(self):
        node = self.stack.pop()
        expression_string = self.in_order(node, "")
        return expression_string


def main():
    tree = ExpTree()
    tree.parsePostfix("x x * 2 + x 1 + /")
    print(tree.toInFix())


if __name__ == "__main__":
    main()
