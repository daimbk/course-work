# approach is the same as simple dictionary as same data structure implementation is used
# space complexity: O(Vertices + Edges) hence O((len(listA) + 1) * (len(listB) + 1))

from collections import defaultdict


def test_display(text, adjacency_list, rows, cols):
    print(text)
    for i in range(rows):
        row_values = " ".join(f"{adjacency_list[i][j]:2}" for j in range(cols))
        print(row_values)


def edit_distance_recursive(row, col, adjacency_list, listA, listB):
    if adjacency_list[row][col] == -1:
        if adjacency_list[row - 1][col] == -1:
            costDel = edit_distance_recursive(
                row - 1, col, adjacency_list, listA, listB) + 1
        else:
            costDel = adjacency_list[row - 1][col] + 1

        if adjacency_list[row][col - 1] == -1:
            costInsert = edit_distance_recursive(
                row, col - 1, adjacency_list, listA, listB) + 1
        else:
            costInsert = adjacency_list[row][col - 1] + 1

        if adjacency_list[row - 1][col - 1] == -1 and listA[row - 1] == listB[col - 1]:
            cost = edit_distance_recursive(
                row - 1, col - 1, adjacency_list, listA, listB)
        elif adjacency_list[row - 1][col - 1] == -1 and listA[row - 1] != listB[col - 1]:
            cost = edit_distance_recursive(
                row - 1, col - 1, adjacency_list, listA, listB) + 1
        elif adjacency_list[row - 1][col - 1] != -1 and listA[row - 1] == listB[col - 1]:
            cost = adjacency_list[row - 1][col - 1]
        elif adjacency_list[row - 1][col - 1] != -1 and listA[row - 1] != listB[col - 1]:
            cost = adjacency_list[row - 1][col - 1] + 1

        adjacency_list[row][col] = min(costDel, costInsert, cost)

    return adjacency_list[row][col]


# ----------------------test 1---------------------
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

print("TEST 1")
print(f"Word 1 : {listA}\nWord 2 : {listB}")
test_display("BEFORE", adjacency_list, len(listA) + 1, len(listB) + 1)
edit_distance_recursive(len(listA), len(listB), adjacency_list, listA, listB)
test_display("\nAFTER", adjacency_list, len(listA) + 1, len(listB) + 1)


# ----------------------test 2---------------------
listA = ["S", "I", "T", "T", "I", "N", "G"]
listB = ["K", "I", "T", "T", "E", "N"]

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

print("\nTEST 2")
print(f"Word 1 : {listA}\nWord 2 : {listB}")
test_display("BEFORE", adjacency_list, len(listA) + 1, len(listB) + 1)
edit_distance_recursive(len(listA), len(listB), adjacency_list, listA, listB)
test_display("\nAFTER", adjacency_list, len(listA) + 1, len(listB) + 1)


# ----------------------test 3---------------------
listA = ["C", "O", "D", "I", "N", "G"]
listB = ["L", "A", "N", "G", "U", "A", "G", "E"]

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

print("\nTEST 3")
print(f"Word 1 : {listA}\nWord 2 : {listB}")
test_display("BEFORE", adjacency_list, len(listA) + 1, len(listB) + 1)
edit_distance_recursive(len(listA), len(listB), adjacency_list, listA, listB)
test_display("\nAFTER", adjacency_list, len(listA) + 1, len(listB) + 1)
