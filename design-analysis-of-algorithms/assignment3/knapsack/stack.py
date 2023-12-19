'''
Stack: Would not recommend. Have to force a stack to be DP. (Why even?)
Time Complexity: O(numOfItems * maxWeight)
Space Complexity:  O(maxWeight + numOfItems)

Pros:
Better memory usage as recursive calls are imitated only when needed
Data obtainable as pops only from top (less indexing issues)

Cons:
No visualization as a 2d matrix shows
More difficult to implement than 2d matrix
Stack has to be reprocessed to get result
'''


def knapsack_dynamic_stack(numOfItems, maxWeight, values, weights):
    cost = [0] * (maxWeight + 1)

    for i in range(1, numOfItems + 1):
        new_cost = cost.copy()
        for w in range(maxWeight + 1):
            if weights[i - 1] <= w:
                new_cost[w] = max(cost[w], values[i - 1] +
                                  cost[w - weights[i - 1]])
        cost = new_cost

    total_value = cost[maxWeight]
    included_items = reconstruct_solution_stack(
        cost, weights, numOfItems, maxWeight)

    return total_value, included_items


def reconstruct_solution_stack(cost, weights, numOfItems, maxWeight):
    included_items = []
    i, w = numOfItems, maxWeight

    while i > 0 and w > 0:
        if cost[w] != cost[w - 1]:
            included_items.append(i)
            w -= weights[i - 1]
            i -= 1
        else:
            i -= 1

    return included_items


def test_display_dynamic_stack(result, weights, values):
    total_value, included_items = result
    print(
        f"\nResult: Total Value: {total_value}, Included Items: {included_items}")
    for i in included_items:
        print(f"Item {i}: Weight {weights[i - 1]}, Value {values[i - 1]}")


# initialize data
numOfItems = 5
maxWeightCapacity = 11
values = [0, 1, 6, 18, 22, 28]
weights = [0, 1, 2, 5, 6, 7]

result = knapsack_dynamic_stack(numOfItems, maxWeightCapacity, values, weights)
test_display_dynamic_stack(result, weights, values)
