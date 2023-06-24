# Assignment 4: Graphs
# Daim Bin Khalid
# 251686775

class VertexNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class EdgeNode:
    def __init__(self, index, next=None):
        self.index = index
        self.next = next


class Graph:
    def __init__(self):
        self.vertices = []

    def add_user(self, name):
        user = VertexNode(name)
        self.vertices.append(user)

    def add_friend(self, username, friend_name):

        user = None
        friend_node = None
        # search friend in users
        for node in self.vertices:
            if node.data == username:
                user = node

            if node.data == friend_name:
                friend_node = node

        # check if user or friend doesn't exist
        if user == None:
            print("User doesn't exist")
            return
        elif friend_node == None:
            print("No user found of such name. Cannot add friend.")
            return

        iterator = user

        while iterator.next is not None:
            iterator = iterator.next

        iterator.next = EdgeNode(friend_node)

    def remove_user(self, username):

        for index, node in enumerate(self.vertices):
            if node.data == username:
                removing_node = node
                removing_index = index
                break

        # find the users the person being deleted is friends of
        for name in self.vertices:
            if name.next is not None:
                iterator = name.next

                if iterator.index == removing_node:
                    name.next = iterator.next
                else:
                    while iterator.next is not None:
                        if iterator.next.index == removing_node:
                            iterator.next = iterator.next.next
                            break

                        iterator = iterator.next

        self.vertices.pop(removing_index)

    def remove_friend(self, username, friend_name):

        user = None
        removing_node = None
        for node in self.vertices:
            if node.data == username:
                user = node

            if node.data == friend_name:
                removing_node = node

                if user is not None and removing_node is not None:
                    break

        # check if user or friend doesn't exist
        if user == None:
            print("User doesn't exist")
            return
        elif removing_node == None:
            print("No user found of such name. Cannot remove friend.")
            return

        for node in self.vertices:
            if node.data == user.data:
                if node.next is not None:
                    iterator = node.next

                    if iterator.index == removing_node:
                        node.next = iterator.next

                    while iterator.next is not None:
                        if iterator.next.index == removing_node:
                            iterator.next = iterator.next.next

                        iterator = iterator.next

                    break

    def print_graph(self):
        counter = 1
        for user in self.vertices:
            if user.next == None:
                print(f'{counter} {user.data}')
            else:
                print(f'{counter} {user.data}', end=": ")
                iterator = user.next

                while iterator is not None:
                    if iterator.next is not None:
                        print(iterator.index.data, end=", ")
                    else:
                        print(iterator.index.data)

                    iterator = iterator.next

            counter += 1

    def dfs_fof(self, username):
        visited = set()

        def dfs(user, visited):
            if user in visited:
                return

            visited.add(user)

            for vertex in self.vertices:
                if vertex.data == user:
                    user = vertex
                    break
            print(user.data)

            iterator = user.next
            while iterator is not None:
                dfs(iterator.index, visited)
                iterator = iterator.next

        for node in self.vertices:
            if node.data == username:
                dfs(node, visited)
                break

    def bfs_fof(self, username):
        visited = set()
        queue = []

        for node in self.vertices:
            if node.data == username:
                queue.append(node)
                break

        while len(queue) > 0:
            user = queue.pop(0)
            if user in visited:
                continue

            visited.add(user)
            friends = []

            iterator = user.next
            while iterator is not None:
                if iterator.index not in visited:
                    queue.append(iterator.index)
                    friends.append(iterator.index.data)

                iterator = iterator.next

            print(user.data + ": " + ", ".join(friends))


def main():
    graph = Graph()
    print("||| Social Network |||")
    print(
        "Commands:\n\tadd_user [name]\n\tadd_friend [username] [friend-name]")
    print("\tremove_user [username]\n\tremove_friend [username] [friend-name]")
    print("\tprint_graph\n\tdfs_fof [username]\n\tbfs_fof [username]")

    command = input("Enter Command:\n")

    while command != "quit":
        command_list = command.split(' ')

        if command_list[0] == "add_user":
            graph.add_user(command_list[1])
        elif command_list[0] == "add_friend":
            graph.add_friend(command_list[1], command_list[2])
        elif command_list[0] == "remove_user":
            graph.remove_user(command_list[1])
        elif command_list[0] == "remove_friend":
            graph.remove_friend(command_list[1], command_list[2])
        elif command_list[0] == "print_graph":
            print()
            graph.print_graph()
            print()
        elif command_list[0] == "dfs_fof":
            graph.dfs_fof(command_list[1])
        elif command_list[0] == "bfs_fof":
            graph.bfs_fof(command_list[1])
        else:
            print("Command is Invalid")
        command = input()


if __name__ == "__main__":
    main()
