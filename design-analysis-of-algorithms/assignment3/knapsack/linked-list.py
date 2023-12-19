'''
Linked List: Not recommended for DP. Very painful to implement.
Time Complexity: O(numOfItems^2)
Space Complexity:  O(numOfItems * maxWeight) due to the linked list and the 2D matrix used for indexing.

Pros:
Memory is only used for needed nodes (no empty cells)
Less space used for nodes

Cons:
Difficult to implement
High time complexity
More time complexity for indexing
Have to declare separate array to have indexing
'''


class Node:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.next = None


def create_linked_list(weights, values):
    head = None
    tail = None
    for weight, value in zip(weights, values):
        node = Node(weight, value)
        if tail is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def test_display(text, weights, values, matrix):
    column_headings = [f"W({i}){' ':>4}" for i in range(len(matrix[0]))]
    print(f"{text}\n\t{' ':>4}{' '.join(column_headings)}")

    for weight, value, row in zip(weights, values, matrix):
        row_values = " ".join(
            f"{element if element is not None else ' ':>8}" for element in row)
        print(f"{weight}({value}) {row_values}{' ':>2}")


def knapsack_linked_list(items, maxWeight, costMatrix):
    if items[-1].weight > maxWeight:
        if costMatrix[len(items) - 1][maxWeight] is None:
            costMatrix[len(items) - 1][maxWeight] = knapsack_linked_list(
                items[:-1], maxWeight, costMatrix)
        return costMatrix[len(items) - 1][maxWeight]
    else:
        if costMatrix[len(items) - 1][maxWeight] is None:
            costMatrix[len(items) - 1][maxWeight] = knapsack_linked_list(
                items[:-1], maxWeight, costMatrix)

        if costMatrix[len(items) - 1][maxWeight - items[-1].weight] is None:
            costMatrix[len(items) - 1][maxWeight - items[-1].weight] = knapsack_linked_list(
                items[:-1], maxWeight - items[-1].weight, costMatrix)

        return max(costMatrix[len(items) - 1][maxWeight], items[-1].value +
                   costMatrix[len(items) - 1][maxWeight - items[-1].weight])


# helper function to convert linked list to list for indexing
def linked_list_to_list(node):
    result = []
    while node is not None:
        result.append(node)
        node = node.next
    return result


# initialize linked list
numOfItems = 5
maxWeightCapacity = 11
values = [0, 1, 6, 18, 22, 28]
weights = [0, 1, 2, 5, 6, 7]

item_list = create_linked_list(weights, values)
item_list_as_list = linked_list_to_list(item_list)
costMatrix_linked_list = [[None for _ in range(maxWeightCapacity + 1)]
                          for _ in range(numOfItems + 1)]

# filling of base rows
for i in range(maxWeightCapacity + 1):
    costMatrix_linked_list[0][i] = 0

# filling of base cols
for j in range(numOfItems + 1):
    costMatrix_linked_list[j][0] = 0

test_display("BEFORE", weights, values, costMatrix_linked_list)
knapsack_linked_list(item_list_as_list, maxWeightCapacity,
                     costMatrix_linked_list)
test_display("\nAFTER", weights, values, costMatrix_linked_list)
