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

    if (numOfItems, maxWeight) in costDict:
        return costDict[(numOfItems, maxWeight)]

    if weights[numOfItems - 1] > maxWeight:
        costDict[(numOfItems, maxWeight)] = knapsack(
            numOfItems - 1, maxWeight, values, weights, costDict)
        return costDict[(numOfItems, maxWeight)]
    else:
        subproblem1 = knapsack(numOfItems - 1, maxWeight,
                               values, weights, costDict)
        subproblem2 = knapsack(numOfItems - 1, maxWeight -
                               weights[numOfItems - 1], values, weights, costDict)

        costDict[(numOfItems, maxWeight)] = max(
            subproblem1, values[numOfItems - 1] + subproblem2)
        return costDict[(numOfItems, maxWeight)]


# initialize data and dictionary
maxWeightCapacity = 11
values = [1, 6, 18, 22, 28]
weights = [1, 2, 5, 6, 7]
numOfItems = len(values)

costDict = {}


def test_display(text, dictionary):
    print(f"{text}")
    for weightNum in range(maxWeightCapacity + 1):
        print(f"W({weightNum}) ", end=" ")
    print()

    for i in range(numOfItems + 1):
        for weightNum in range(maxWeightCapacity + 1):
            if (i, weightNum) in dictionary:
                print(dictionary[(i, weightNum)], "   ", end=" ")
            else:
                print("     ", end=" ")
        print()


test_display("BEFORE", costDict)
result = knapsack(numOfItems, maxWeightCapacity, values, weights, costDict)
test_display("\nAFTER", costDict)
print("\nResult:", result)
