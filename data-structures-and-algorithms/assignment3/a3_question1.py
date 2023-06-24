# Assignment 3: Binary Search Trees
# Name: Daim Bin Khalid
# Roll no.: 251686775
# Question 1: Movie Database

class CastNode:
    """Node for creating singly linked list of actors in a movie"""

    def __init__(self, actor, next=None):
        self.actor = actor
        self.next = next


class MovieNode:
    """Contains record of the movie"""

    def __init__(self, title, cast, year, duration):
        self.title = title
        # cast var stores the header of the linked list containing cast nodes
        self.cast = cast
        self.year = year
        self.duration = duration


class BSTNode:
    def __init__(self, parent=None, data=None, left=None, right=None):
        self.parent = parent
        # data var stores the MovieNode containing movie info
        self.data = data
        self.left = left
        self.right = right
        self.height = 0


class BinarySearchTree:
    def __init__(self):
        self.root = BSTNode()
        self.size = 0

    def add_movie(self, title, year, duration):
        # check to find if movie is already added using BSTs
        if self.root.data is not None:
            node_queue = [self.root]

            while len(node_queue) > 0:
                node = node_queue.pop(0)
                if node.data.title == title:
                    print("Movie already added.")
                    return

                if node.left is not None:
                    node_queue.append(node.left)

                if node.right is not None:
                    node_queue.append(node.right)

        # add movie to the tree
        node = MovieNode(title, None, year, duration)

        if self.root.data is None:
            self.root.data = node
            self.size += 1
            self.root.height = 0
            return

        check_node = self.root
        insert_done = False

        while not insert_done:
            if title[0] < check_node.data.title[0]:
                if check_node.left == None:
                    check_node.left = BSTNode(check_node, node)
                    insert_done = True
                    self.size += 1
                    check_node.left.height = check_node.height + 1
                else:
                    check_node = check_node.left

            else:
                if check_node.right == None:
                    check_node.right = BSTNode(check_node, node)
                    insert_done = True
                    self.size += 1
                    check_node.right.height = check_node.height + 1
                else:
                    check_node = check_node.right

    def add_actor(self, movie, name):
        """
        Adds an actor to the cast list of the movie title provided.
        The actor is added as a node connected in a linked list.
        """

        if self.root.data is None:
            print("No movie data added yet.")
            return
        else:
            node_queue = [self.root]

        # get the node containing the movie using breadth-first-search
        while len(node_queue) > 0:
            node = node_queue.pop(0)
            if node.data.title == movie:
                break

            if node.left is not None:
                node_queue.append(node.left)

            if node.right is not None:
                node_queue.append(node.right)

        # add actor to the cast list
        if node.data.cast is None:
            node.data.cast = CastNode(name)
        else:
            iterator = node.data.cast
            while iterator.next is not None:
                iterator = iterator.next

            iterator.next = CastNode(name)

    def delete_movie(self, title):
        """
        Delete the BSTNode containing the movie records entered
        """

        def find_minimum(node):
            current = node
            while current.left is not None:
                current = current.left
            return current

        def get_height(node):
            if node is None:
                return -1
            return node.height

        def deleteNode(node, title):
            if node is None:
                return node

            if title < node.data.title:
                node.left = deleteNode(node.left, title)
            elif title > node.data.title:
                node.right = deleteNode(node.right, title)
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
                node.right = deleteNode(node.right, temp.data.title)

            if node is None:
                return node

            node.height = 1 + max(get_height(node.left),
                                  get_height(node.right))

        deleteNode(self.root, title)

    def find_movie(self, title):
        if self.root.data is None:
            print("No movie data added yet.")
            return
        else:
            node_queue = [self.root]

        found = False
        while len(node_queue) > 0:
            node = node_queue.pop(0)
            if node.data.title == title:
                found = True
                break

            if node.left is not None:
                node_queue.append(node.left)

            if node.right is not None:
                node_queue.append(node.right)

        if not found:
            print("Movie not found.")
            return

        # Display the details of the movie
        print(f'\nMovie: {node.data.title}\nYear of release: {node.data.year}')
        print(f'Duration: {node.data.duration} minutes')
        print("Cast: ", end="")
        iterator = node.data.cast
        while iterator is not None:
            if iterator.next is None:
                print(iterator.actor)
                iterator = iterator.next
                print()
            else:
                print(iterator.actor, end=", ")
                iterator = iterator.next

    def find_actor(self, actor):
        """Displays all movies the actor has appeared in"""

        # list to store actor's movies
        movies = []

        if self.root.data is None:
            print("No movie data added yet.")
            return
        else:
            node_queue = [self.root]

        # using bfs search to navigate the tree
        found = False
        while len(node_queue) > 0:
            node = node_queue.pop(0)
            iterator = node.data.cast
            while iterator is not None:
                if iterator.actor == actor:
                    movies.append(node.data.title)
                    found = True
                iterator = iterator.next

            if node.left is not None:
                node_queue.append(node.left)

            if node.right is not None:
                node_queue.append(node.right)

        if not found:
            print("No movies in database of this actor.")
        else:
            print(f'\n{actor} has appeared in:')
            for movie in movies:
                print(movie)
            print()

    def print_movies(self, root):
        """
        Prints movies in sorted order using in-order traversal
        """

        print("\nMovies in Database:")

        def in_order(root):
            if root == None:
                return
            else:
                in_order(root.left)
                print(root.data.title)
                in_order(root.right)

        in_order(root)
        print()

    def isBSTBalanced(self, root):
        """Returns true if the tree is balanced and no otherwise"""

        # height is checked for each leaf node
        def get_height(node):
            if node is None:
                return 0

            return 1 + max(get_height(node.left), get_height(node.right))

        if root is None:
            return True

        # Check if left and right subtrees are balanced
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if root.left is None:
            return abs(get_height(root.right)) <= 1 and self.isBSTBalanced(root.right)

        if root.right is None:
            return abs(get_height(root.left)) <= 1 and self.isBSTBalanced(root.left)

        return abs(get_height(root.left) - get_height(root.right)) <= 1 and self.isBSTBalanced(root.left) and self.isBSTBalanced(root.right)

    def balance_tree(self, node):
        """Tree balancing using AVL rotation methods"""

    # ======== Tree Balancing Support Functions ========
        def get_height(node):
            if node is None:
                return -1
            return node.height

        def get_balance_factor(node):
            if node is None:
                return 0
            return get_height(node.left) - get_height(node.right)

        def left_rotate(node):
            right_child = node.right
            node.right = right_child.left
            right_child.left = node
            node.height = max(get_height(node.left),
                              get_height(node.right)) + 1
            right_child.height = max(get_height(
                right_child.left), get_height(right_child.right)) + 1
            return right_child

        def right_rotate(node):
            left_child = node.left
            node.left = left_child.right
            left_child.right = node
            node.height = max(get_height(node.left),
                              get_height(node.right)) + 1
            left_child.height = max(get_height(
                left_child.left), get_height(left_child.right)) + 1
            return left_child

        def left_right_rotate(node):
            node.left = left_rotate(node.left)
            return right_rotate(node)

        def right_left_rotate(node):
            node.right = right_rotate(node.right)
            return left_rotate(node)

        if node is None:
            return None

        balance_factor = get_balance_factor(node)
        if balance_factor >= -1 and balance_factor <= 1:
            return node

        if balance_factor > 1 and get_balance_factor(node.left) >= 0:
            return right_rotate(node)
        elif balance_factor > 1 and get_balance_factor(node.left) < 0:
            return left_right_rotate(node)
        elif balance_factor < -1 and get_balance_factor(node.right) <= 0:
            return left_rotate(node)
        elif balance_factor < -1 and get_balance_factor(node.right) > 0:
            return right_left_rotate(node)
        return node

    def insert_movie_balanced(self, title, year, duration):
        """Insert movie in BST but resultant BST should be balanced. 
        IsBSTBalanced() should return true before executing this function"""

        self.balance_tree(self.root)
        print(f'Is the BST Balanced: {self.isBSTBalanced(self.root)}')
        self.add_movie(title, year, duration)

    def delete_movie_balanced(self, title):
        """Delete movie in BST but resultant BST should be balanced. 
        IsBSTBalanced() should return true before executing this function"""

        self.balance_tree(self.root)
        print(f'Is the BST Balanced: {self.isBSTBalanced(self.root)}')
        self.delete_movie(title)

    # ======= BONUS SECTION =======
    def save(self, filename):
        """
        Saves the movie database info to a text-file
        Saving format:
        title year duration
        cast
        """

        text_file = open(filename + '.txt', 'a+')

        if self.root.data is None:
            print("No movie data added yet.")
            return
        else:
            node_queue = [self.root]

        # navigate the tree using breadth-first-search
        while len(node_queue) > 0:
            node = node_queue.pop(0)
            print(node.data.title, node.data.year,
                  node.data.duration, file=text_file)

            # save a blank line if no cast is added
            cast_iterator = node.data.cast
            if cast_iterator is None:
                text_file.write("\n")

            # iterate through cast linked list
            while cast_iterator is not None:
                if cast_iterator.next is None:
                    print(cast_iterator.actor, file=text_file)

                else:
                    print(cast_iterator.actor, file=text_file, end=" ")
                cast_iterator = cast_iterator.next

            if node.left is not None:
                node_queue.append(node.left)

            if node.right is not None:
                node_queue.append(node.right)

        text_file.close()

    def load(self, filename):
        """Loads the movie database info to a text-file"""

        text_file = open(filename + '.txt', 'r')

        line = text_file.readline()
        while line != "":
            line = line.rstrip("\n").split()
            movie_name = line[0]
            self.add_movie(line[0], line[1], line[2])

            # adding cast to node
            line = text_file.readline()
            if line != "\n":
                line = line.rstrip("\n").split()

            for actor in line:
                self.add_actor(movie_name, actor)

            line = text_file.readline()

        text_file.close()


def main():
    database = BinarySearchTree()
    print("||| Movie Database |||")
    print(
        "Commands:\n\tadd_movie [title] [year] [duration]\n\tdelete_movie [title]\n\tprint_movies")
    print("\tfind_movie [title]\n\tfind_actor [actor]\n\tisBSTBalanced")
    print("\tbalance_tree\n\tinsert_movie_balanced [title] [year] [duration]")
    print(
        "\tdelete_movie_balanced [title]\n\tsave [filename]\n\tload [filename]")

    command = input("Enter Command:\n")

    while command != "quit":
        command_list = command.split(' ')

        if command_list[0] == "add_movie":
            database.add_movie(
                command_list[1], command_list[2], command_list[3])
        elif command_list[0] == "add_actor":
            database.add_actor(command_list[1], command_list[2])
        elif command_list[0] == "delete_movie":
            database.delete_movie(command_list[1])
        elif command_list[0] == "print_movies":
            database.print_movies(database.root)
        elif command_list[0] == "find_movie":
            database.find_movie(command_list[1])
        elif command_list[0] == "find_actor":
            database.find_actor(command_list[1])
        elif command_list[0] == "isBSTBalanced":
            print(database.isBSTBalanced(database.root))
        elif command_list[0] == "balance_tree":
            database.balance_tree(database.root)
        elif command_list[0] == "insert_movie_balanced":
            database.insert_movie_balanced(
                command_list[1], command_list[2], command_list[3])
        elif command_list[0] == "delete_movie_balanced":
            database.delete_movie_balanced(command_list[1])
        elif command_list[0] == "save":
            database.save(command_list[1])
        elif command_list[0] == "load":
            database.load(command_list[1])
        else:
            print("command is invalid")
        command = input()


if __name__ == '__main__':
    main()
