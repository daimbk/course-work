# Lab 11
# Name: Daim Bin Khalid
# Roll no.: 251686775

class BSTNode:
    def __init__(self, parent=None, data=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = BSTNode()
        self.size = 0

    def insert(self, data):
        if self.root.data is None:
            self.root.data = data
            self.size += 1

        else:
            node = BSTNode(None, data, None, None)

            check_node = self.root
            insert_done = False
            while not insert_done:
                if data < check_node.data:
                    if check_node.left == None:
                        check_node.left = node
                        node.parent = check_node
                        insert_done = True
                        self.size += 1
                    else:
                        check_node = check_node.left

                if data > check_node.data:
                    if check_node.right == None:
                        check_node.right = node
                        node.parent = check_node
                        insert_done = True
                        self.size += 1
                    else:
                        check_node = check_node.right

    def delete(self, data):

        def find_minimum(node):
            current = node
            while (current.left is not None):
                current = current.left

            return current

        def deleteNode(node, data):
            if node is None:
                return node

            if data < node.data:
                node.left = deleteNode(node.left, data)
            elif (data > node.data):
                node.right = deleteNode(node.right, data)
            else:
                if node.left is None:
                    temp = node.right
                    node = None
                    return temp

                elif node.right is None:
                    temp = node.left
                    node = None
                    return temp

                temp = find_minimum(node.right)

                node.data = temp.data
                node.right = deleteNode(node.right, temp.data)

            return node

        deleteNode(self.root, data)

    def search(self, data):
        check_node = self.root

        while True:
            if data == check_node.data:
                return check_node
            elif data < check_node.data:
                check_node = check_node.left
                if check_node is None:
                    return None
            else:
                check_node = check_node.right
                if check_node is None:
                    return None

    def in_order(self):
        node = self.root

        def iterate(node):
            if node == None:
                return
            else:
                iterate(node.left)
                print(node.data, end=' ')
                iterate(node.right)

        iterate(node)

    def pre_order(self):
        node = self.root

        def iterate(node):
            if node == None:
                return
            else:
                print(node.data, end=' ')
                iterate(node.left)
                iterate(node.right)

        iterate(node)

    def post_order(self):
        node = self.root

        def iterate(node):
            if node == None:
                return
            else:
                iterate(node.left)
                iterate(node.right)
                print(node.data, end=' ')

        iterate(node)

    def get_parent(self, data):
        node = self.search(data)
        return node.parent

    def height(self):
        def depth(node):
            if node == None:
                return 0

            else:
                left_tree_height = depth(node.left)
                right_tree_height = depth(node.right)

                if left_tree_height > right_tree_height:
                    return left_tree_height + 1
                else:
                    return right_tree_height + 1

        return depth(self.root)


def main():
    tree = BST()
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)

    tree.in_order()
    print()
    tree.pre_order()
    print()
    tree.post_order()

    print(f'Height: {tree.height()}')
    print(f'Searching 6 in tree: {tree.search(6).data}')
    print(f'Parent of 6: {tree.get_parent().data}')
    tree.delete(8)


main()
