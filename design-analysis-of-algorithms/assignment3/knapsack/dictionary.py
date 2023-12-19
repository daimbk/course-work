'''
Dictionary: can be used as a 2d matrix alternative. Same complexity and almost easy implementation
Time Complexity: O(numOfItems * maxWeight)
Space Complexity: O(numOfItems * maxWeight)

Pros:
Good data structure for DP usage
Simple access to needed index

Cons:
Could prove to be complex for larger datasets
'''


def knapsack(numOfItems, maxWeight, values, weights, costDict):
    if numOfItems == 0 or maxWeight == 0:
        return 0

    if (weights[numOfItems - 1] > maxWeight):
        subproblem = (numOfItems - 1, maxWeight)
        if costDict.get(subproblem) is None:
            costDict[subproblem] = knapsack(
                *subproblem, values, weights, costDict)
        return costDict[subproblem]
    else:
        subproblem1 = (numOfItems - 1, maxWeight)
        if costDict.get(subproblem1) is None:
            costDict[subproblem1] = knapsack(
                *subproblem1, values, weights, costDict)

        subproblem2 = (numOfItems - 1, maxWeight - weights[numOfItems - 1])
        if costDict.get(subproblem2) is None:
            costDict[subproblem2] = knapsack(
                *subproblem2, values, weights, costDict)

        costDict[(numOfItems, maxWeight)] = max(costDict[subproblem1],
                                                values[numOfItems - 1] + costDict[subproblem2])
        return costDict[(numOfItems, maxWeight)]


# initialize data and dictionary
numOfItems = 5
maxWeightCapacity = 11
values = [0, 1, 6, 18, 22, 28]
weights = [0, 1, 2, 5, 6, 7]

costDict = {}


def test_display(text, weights, values, dictionary):
    # display weight capacity as column headings with fixed size
    column_headings = [f"W({i}){' ':>4}" for i in range(maxWeightCapacity + 1)]
    print(f"{text}\n\t{' ':>4}{' '.join(column_headings)}")

    # display weights, values as rows with fixed size
    # display dictionary uniformly
    for i in range(numOfItems + 1):
        row_values = " ".join(
            f"{dictionary.get((i, j), ' '):>8}" for j in range(maxWeightCapacity + 1))
        print(f"{weights[i]}({values[i]}) {row_values}{' ':>2}")


test_display("BEFORE", weights, values, costDict)
result = knapsack(numOfItems, maxWeightCapacity, values, weights, costDict)
test_display("\nAFTER", weights, values, costDict)
print("\nResult:", result)
