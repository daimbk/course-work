# Lab 10
#===================================
# Name   : Daim Bin Khalid
# Roll no: 251686775
# Section: C
# Date   : 13/12/2022
#===================================
#===================================

from queue import Queue

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def AddLeft(self, node, data):
        new_node = Node(data, node)
        node.left = new_node
        self.size += 1

    def GetLeft(self, node):
        return node.left

    def AddRight(self, node, data):
        new_node = Node(data, node)
        node.right = new_node
        self.size += 1

    def GetRight(self, node):
        return node.right

    def SetRoot(self, data):
        self.root = Node(data)
        self.size += 1

    def GetRoot(self):
        return self.root

    def is_Leaf(self, node):
        if node.left is None and node.right is None:
            return True
        else:
            return False

    def GetParent(self, node):
        return node.parent

    def __len__(self):
        return self.size


# Question 2: Manually Creating a Tree
Tree = BinaryTree()
Tree.SetRoot(11)
root = Tree.GetRoot()
Tree.AddLeft(root, 6)
Tree.AddRight(root, 19)

node = Tree.GetLeft(root)
Tree.AddLeft(node, 4)
node = Tree.GetLeft(node)
Tree.AddRight(node, 5)

node = Tree.GetLeft(root)
Tree.AddRight(node, 8)
node = Tree.GetRight(node)
Tree.AddRight(node, 10)

node = Tree.GetRight(root)
Tree.AddLeft(node, 17)
Tree.AddRight(node, 43)

node = Tree.GetRight(node)
Tree.AddLeft(node, 31)
Tree.AddRight(node, 49)


# Question 3: Traversals
def post_order(node):
    if node == None:
        return
    else:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end=' ')

def pre_order(node):
    if node == None:
        return
    else:
        print(node.data, end=' ')
        pre_order(node.left)
        pre_order(node.right)

def in_order(node):
    if node == None:
        return
    else:
        in_order(node.left)
        print(node.data, end=' ')
        in_order(node.right)

def breadth_first_search(root):
   if root is not None:
        node_queue = [root]

        while len(node_queue) > 0:
            node = node_queue.pop(0)
            print(node.data, end=' ')

            if node.left is not None:
                node_queue.append(node.left)

            if node.right is not None:
                node_queue.append(node.right)


pre_order(root)
print()
post_order(root)
print()
in_order(root)
print()
breadth_first_search(root)
