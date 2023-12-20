'''
Queue: Okish for knapsack as very similar to 2d matrix 
Time Complexity:  O(numOfItems * maxWeight)
Space Complexity:   O(numOfItems * maxWeight)

Pros:
Dequeue is used as queue which is very similar to 2d matrix approach

Cons:
Unnecessary complexity added to 2d matrix approach
'''

from collections import deque


def knapsack(numOfItems, maxWeight, values, weights, costQueue):
    if weights[numOfItems-1] > maxWeight:
        if costQueue[numOfItems - 1][maxWeight] is None:
            costQueue[numOfItems][maxWeight] = knapsack(
                numOfItems - 1, maxWeight, values, weights, costQueue)
        return costQueue[numOfItems][maxWeight]

    else:
        if costQueue[numOfItems - 1][maxWeight] is None:
            costQueue[numOfItems][maxWeight] = knapsack(
                numOfItems - 1, maxWeight, values, weights, costQueue)

        if costQueue[numOfItems - 1][maxWeight - weights[numOfItems-1]] is None:
            costQueue[numOfItems - 1][maxWeight - weights[numOfItems-1]] = knapsack(
                numOfItems - 1, maxWeight - weights[numOfItems-1], values, weights, costQueue)

        costQueue[numOfItems][maxWeight] = max(
            costQueue[numOfItems - 1][maxWeight], values[numOfItems-1] + costQueue[numOfItems - 1][maxWeight - weights[numOfItems-1]])
        return costQueue[numOfItems][maxWeight]


# initialize data and queue
maxWeightCapacity = 11
values = [1, 6, 18, 22, 28]
weights = [1, 2, 5, 6, 7]
numOfItems = len(values)

# using deque as a queue
costQueue = [deque([None] * (maxWeightCapacity + 1))
             for _ in range(numOfItems + 1)]

# filling of base rows
for i in range(maxWeightCapacity + 1):
    costQueue[0][i] = 0

# filling of base cols
for j in range(numOfItems + 1):
    costQueue[j][0] = 0


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


test_display("BEFORE", costQueue)
knapsack(numOfItems, maxWeightCapacity, values, weights, costQueue)
test_display("\nAFTER", costQueue)
