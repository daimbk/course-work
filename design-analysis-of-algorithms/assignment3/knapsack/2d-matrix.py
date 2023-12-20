'''
2D Matrix: Optimal data structure
Time Complexity: O(numOfItems * maxWeight)
Space Complexity: O(numOfItems * maxWeight)

Pros:
Simple way to represent a grid
Simple access to needed index
Simple to implement

Cons:
Unused cells in result
'''


def knapsack(numOfItems, maxWeight, values, weights, costMatrix):
    if weights[numOfItems-1] > maxWeight:
        if costMatrix[numOfItems - 1][maxWeight] is None:
            costMatrix[numOfItems][maxWeight] = knapsack(
                numOfItems - 1, maxWeight, values, weights, costMatrix)
        return costMatrix[numOfItems][maxWeight]

    else:
        if costMatrix[numOfItems - 1][maxWeight] is None:
            costMatrix[numOfItems][maxWeight] = knapsack(
                numOfItems - 1, maxWeight, values, weights, costMatrix)

        if costMatrix[numOfItems - 1][maxWeight - weights[numOfItems-1]] is None:
            costMatrix[numOfItems - 1][maxWeight - weights[numOfItems-1]] = knapsack(
                numOfItems - 1, maxWeight - weights[numOfItems-1], values, weights, costMatrix)

        costMatrix[numOfItems][maxWeight] = max(
            costMatrix[numOfItems - 1][maxWeight], values[numOfItems-1] + costMatrix[numOfItems - 1][maxWeight - weights[numOfItems-1]])
        return costMatrix[numOfItems][maxWeight]


# initialize data and 2d matrix
maxWeightCapacity = 11
values = [1, 6, 18, 22, 28]
weights = [1, 2, 5, 6, 7]
numOfItems = len(values)

costMatrix = [[None for _ in range(maxWeightCapacity + 1)]
              for _ in range(numOfItems + 1)]

# filling of base rows
for i in range(maxWeightCapacity + 1):
    costMatrix[0][i] = 0

# filling of base cols
for j in range(numOfItems + 1):
    costMatrix[j][0] = 0


def test_display(text, matrix):
    print(f"{text}")
    for weightNum in range(maxWeightCapacity + 1):
        print(f"W({weightNum}) ", end=" ")
    print()

    for row in matrix:
        for col in row:
            if col != None:
                print(col, "   ", end=" ")
            else:
                print("     ", end=" ")
        print()


test_display("BEFORE", costMatrix)
knapsack(numOfItems, maxWeightCapacity, values, weights, costMatrix)
test_display("\nAFTER", costMatrix)
