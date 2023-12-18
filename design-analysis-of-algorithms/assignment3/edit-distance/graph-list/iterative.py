# approach is the same as simple dictionary as same data structure implementation is used
# space complexity: O(Vertices + Edges) hence O((len(listA) + 1) * (len(listB) + 1))

from collections import defaultdict


def test_display(text, adjacency_list, rows, cols):
    print(text)
    for i in range(rows):
        row_values = " ".join(f"{adjacency_list[i][j]:2}" for j in range(cols))
        print(row_values)


listA = ["M", "A", "T", "H", "S"]
listB = ["A", "R", "T", "S"]

# create graph adjacency list
adjacency_list = defaultdict(dict)

# create nodes for listA and listB
for i in range(len(listA) + 1):
    for j in range(len(listB) + 1):
        adjacency_list[i][j] = -1

# filling of base rows
for j in range(len(listB) + 1):
    adjacency_list[0][j] = j

# filling of base cols
for i in range(len(listA) + 1):
    adjacency_list[i][0] = i

test_display("BEFORE", adjacency_list, len(listA) + 1, len(listB) + 1)


def edit_distance_iterative(adjacency_list, listA, listB, rows, cols):
    for i in range(1, rows):
        for j in range(1, cols):
            if adjacency_list[i][j] == -1:
                costDel = adjacency_list[i - 1][j] + 1
                costInsert = adjacency_list[i][j - 1] + 1
                costReplace = adjacency_list[i - 1][j - 1] + \
                    (0 if listA[i - 1] == listB[j - 1] else 1)
                adjacency_list[i][j] = min(costDel, costInsert, costReplace)


edit_distance_iterative(adjacency_list, listA, listB,
                        len(listA) + 1, len(listB) + 1)
test_display("\nAFTER", adjacency_list, len(listA) + 1, len(listB) + 1)
