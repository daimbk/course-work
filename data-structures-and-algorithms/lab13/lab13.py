# Lab 13: Hash Tables
# Daim Bin Khalid
# 251686775

class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class HashTable:
    def __init__(self):
        # table size 11 in 1D array
        self.table = [[None, None] for list in range(11)]

    def hash_function(self, value):
        # generate key
        key_index = (3 * value + 5) % 11

        # check if index is full
        if self.table[key_index][0] == None:
            self.table[key_index][0] = value
        else:
            # check if there is a second value
            if self.table[key_index][1] == None:
                node = LinkedListNode(value)
                self.table[key_index][1] = node
            else:
                iterator = self.table[key_index][1]
                while iterator.next != None:
                    iterator = iterator.next

                iterator.next = LinkedListNode(value)

    def print_table(self):
        counter = 1
        for index in self.table:
            if index[1] == None:
                print(f'[{counter}] {index[0]}')
            else:
                iterator = index[1]
                print(f'[{counter}] {index[0]}', end=", ")

                while iterator is not None:
                    if iterator.next is not None:
                        print(iterator.data, end=", ")
                    else:
                        print(iterator.data)

                    iterator = iterator.next

            counter += 1


def main():
    table = HashTable()

    # feed data to the table
    data = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]
    for value in data:
        table.hash_function(value)

    table.print_table()


if __name__ == '__main__':
    main()
