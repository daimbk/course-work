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
    if weights[numOfItems] > maxWeight:
        if costQueue[numOfItems - 1][maxWeight] is None:
            costQueue[numOfItems - 1][maxWeight] = knapsack(
                numOfItems - 1, maxWeight, values, weights, costQueue)
        return costQueue[numOfItems - 1][maxWeight]

    else:
        if costQueue[numOfItems - 1][maxWeight] is None:
            costQueue[numOfItems - 1][maxWeight] = knapsack(
                numOfItems - 1, maxWeight, values, weights, costQueue)

        if costQueue[numOfItems - 1][maxWeight - weights[numOfItems]] is None:
            costQueue[numOfItems - 1][maxWeight - weights[numOfItems]] = knapsack(
                numOfItems - 1, maxWeight - weights[numOfItems], values, weights, costQueue)

        return max(costQueue[numOfItems - 1][maxWeight], values[numOfItems] + costQueue[numOfItems - 1][maxWeight - weights[numOfItems]])


# initialize data and queue
numOfItems = 5
maxWeightCapacity = 11
values = [0, 1, 6, 18, 22, 28]
weights = [0, 1, 2, 5, 6, 7]

# using deque as a queue
costQueue = [deque([None] * (maxWeightCapacity + 1))
             for _ in range(numOfItems + 1)]

# filling of base rows
for i in range(maxWeightCapacity + 1):
    costQueue[0][i] = 0

# filling of base cols
for j in range(numOfItems + 1):
    costQueue[j][0] = 0


def test_display(text, weights, values, queue):
    # display weight capacity as column headings with fixed size
    column_headings = [f"W({i}){' ':>4}" for i in range(len(queue[0]))]
    print(f"{text}\n\t{' ':>4}{' '.join(column_headings)}")

    # display weights, values as rows with fixed size
    # display queue uniformly
    for weight, value, row in zip(weights, values, queue):
        row_values = " ".join(
            f"{element if element is not None else ' ':>8}" for element in row)
        print(f"{weight}({value}) {row_values}{' ':>2}")


test_display("BEFORE", weights, values, costQueue)
knapsack(numOfItems, maxWeightCapacity, values, weights, costQueue)
test_display("\nAFTER", weights, values, costQueue)
