'''
Tree: Should not even be used for this. (Refer to Cons)
Time Complexity: O(2^numOfItems)
Space Complexity:  O(2^numOfItems)

Pros:
Can show hierarchy of results

Cons:
Exponential time and space complexity! :(
Difficult to implement and navigate
'''


class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.children = []


def knapsack(numOfItems, maxWeight, values, weights, parentNode):
    if numOfItems == 0 or maxWeight == 0:
        return 0

    if weights[numOfItems - 1] > maxWeight:
        return knapsack(numOfItems - 1, maxWeight, values, weights, parentNode)
    else:
        includeItemNode = TreeNode(values[numOfItems - 1])
        includeItem = values[numOfItems - 1] + knapsack(
            numOfItems - 1, maxWeight - weights[numOfItems - 1], values, weights, includeItemNode)
        parentNode.children.append(includeItemNode)

        excludeItemNode = TreeNode(0)
        excludeItem = knapsack(numOfItems - 1, maxWeight,
                               values, weights, excludeItemNode)
        parentNode.children.append(excludeItemNode)

        parentNode.value = max(includeItem, excludeItem)
        return parentNode.value


# initialize data and tree structure
numOfItems = 5
maxWeightCapacity = 11
values = [0, 1, 6, 18, 22, 28]
weights = [0, 1, 2, 5, 6, 7]

rootNode = TreeNode()


def display_tree(node, depth=0):
    if node is not None:
        print("\t" * depth, f"Value: {node.value}")
        for child in node.children:
            display_tree(child, depth + 1)


knapsack(numOfItems, maxWeightCapacity, values, weights, rootNode)
print("TREE:")
display_tree(rootNode)
