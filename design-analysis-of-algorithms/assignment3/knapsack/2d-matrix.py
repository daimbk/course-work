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
    if (weights[numOfItems] > maxWeight):
        if (costMatrix[numOfItems - 1][maxWeight] is None):
            costMatrix[numOfItems - 1][maxWeight] = knapsack(
                numOfItems - 1, maxWeight, values, weights, costMatrix)
        return costMatrix[numOfItems - 1][maxWeight]

    else:
        if (costMatrix[numOfItems - 1][maxWeight] is None):
            costMatrix[numOfItems - 1][maxWeight] = knapsack(
                numOfItems - 1, maxWeight, values, weights, costMatrix)

        if (costMatrix[numOfItems - 1][maxWeight - weights[numOfItems]] is None):
            costMatrix[numOfItems - 1][maxWeight - weights[numOfItems]] = knapsack(
                numOfItems - 1, maxWeight - weights[numOfItems], values, weights, costMatrix)

        return max(costMatrix[numOfItems - 1][maxWeight], values[numOfItems] + costMatrix[numOfItems - 1][maxWeight - weights[numOfItems]])


# initialize data and 2d matrix
numOfItems = 5
maxWeightCapacity = 11
values = [0, 1, 6, 18, 22, 28]
weights = [0, 1, 2, 5, 6, 7]

costMatrix = [[None for _ in range(maxWeightCapacity + 1)]
              for _ in range(numOfItems + 1)]

# filling of base rows
for i in range(maxWeightCapacity + 1):
    costMatrix[0][i] = 0

# filling of base cols
for j in range(numOfItems + 1):
    costMatrix[j][0] = 0


def test_display(text, weights, values, matrix):
    # display weight capacity as column headings with fixed size
    column_headings = [f"W({i}){' ':>4}" for i in range(len(matrix[0]))]
    print(f"{text}\n\t{' ':>4}{' '.join(column_headings)}")

    # display weights, values as rows with fixed size
    # display matrix uniformly
    for weight, value, row in zip(weights, values, matrix):
        row_values = " ".join(
            f"{element if element is not None else ' ':>8}" for element in row)
        print(f"{weight}({value}) {row_values}{' ':>2}")


test_display("BEFORE", weights, values, costMatrix)
knapsack(numOfItems, maxWeightCapacity, values, weights, costMatrix)
test_display("\nAFTER", weights, values, costMatrix)
