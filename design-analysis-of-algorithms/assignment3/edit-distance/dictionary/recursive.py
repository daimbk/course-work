# approach is the same as graph adjacency list
# space complexity: O(rows * cols)

def test_display(text, dictionary, rows, cols):
    print(text)
    for i in range(rows):
        row_values = " ".join(f"{dictionary[(i, j)]:2}" for j in range(cols))
        print(row_values)


def edit_distance_recursive(row, col, dictionary, listA, listB):
    if dictionary[(row, col)] == -1:
        if dictionary[(row - 1, col)] == -1:
            costDel = edit_distance_recursive(
                row - 1, col, dictionary, listA, listB) + 1
        else:
            costDel = dictionary[(row - 1, col)] + 1

        if dictionary[(row, col - 1)] == -1:
            costInsert = edit_distance_recursive(
                row, col - 1, dictionary, listA, listB) + 1
        else:
            costInsert = dictionary[(row, col - 1)] + 1

        if dictionary[(row - 1, col - 1)] == -1 and listA[row - 1] == listB[col - 1]:
            cost = edit_distance_recursive(
                row - 1, col - 1, dictionary, listA, listB)
        elif dictionary[(row - 1, col - 1)] == -1 and listA[row - 1] != listB[col - 1]:
            cost = edit_distance_recursive(
                row - 1, col - 1, dictionary, listA, listB) + 1
        elif dictionary[(row - 1, col - 1)] != -1 and listA[row - 1] == listB[col - 1]:
            cost = dictionary[(row - 1, col - 1)]
        elif dictionary[(row - 1, col - 1)] != -1 and listA[row - 1] != listB[col - 1]:
            cost = dictionary[(row - 1, col - 1)] + 1

        dictionary[(row, col)] = min(costDel, costInsert, cost)

    return dictionary[(row, col)]


# ----------------------test 1---------------------
listA = ["M", "A", "T", "H", "S"]
listB = ["A", "R", "T", "S"]

# create dictionary
dictionary = {(i, j): -1 for i in range(len(listA) + 1)
              for j in range(len(listB) + 1)}

# filling of base rows
for j in range(len(listB) + 1):
    dictionary[(0, j)] = j

# filling of base cols
for i in range(len(listA) + 1):
    dictionary[(i, 0)] = i

print("TEST 1")
print(f"Word 1 : {listA}\nWord 2 : {listB}")
test_display("BEFORE", dictionary, len(listA) + 1, len(listB) + 1)
edit_distance_recursive(len(listA), len(listB), dictionary, listA, listB)
test_display("\nAFTER", dictionary, len(listA) + 1, len(listB) + 1)


# ----------------------test 2---------------------
listA = ["S", "I", "T", "T", "I", "N", "G"]
listB = ["K", "I", "T", "T", "E", "N"]

# create dictionary
dictionary = {(i, j): -1 for i in range(len(listA) + 1)
              for j in range(len(listB) + 1)}

# filling of base rows
for j in range(len(listB) + 1):
    dictionary[(0, j)] = j

# filling of base cols
for i in range(len(listA) + 1):
    dictionary[(i, 0)] = i

print("\nTEST 2")
print(f"Word 1 : {listA}\nWord 2 : {listB}")
test_display("BEFORE", dictionary, len(listA) + 1, len(listB) + 1)
edit_distance_recursive(len(listA), len(listB), dictionary, listA, listB)
test_display("\nAFTER", dictionary, len(listA) + 1, len(listB) + 1)


# ----------------------test 3---------------------
listA = ["C", "O", "D", "I", "N", "G"]
listB = ["L", "A", "N", "G", "U", "A", "G", "E"]

# create dictionary
dictionary = {(i, j): -1 for i in range(len(listA) + 1)
              for j in range(len(listB) + 1)}

# filling of base rows
for j in range(len(listB) + 1):
    dictionary[(0, j)] = j

# filling of base cols
for i in range(len(listA) + 1):
    dictionary[(i, 0)] = i

print("\nTEST 3")
print(f"Word 1 : {listA}\nWord 2 : {listB}")
test_display("BEFORE", dictionary, len(listA) + 1, len(listB) + 1)
edit_distance_recursive(len(listA), len(listB), dictionary, listA, listB)
test_display("\nAFTER", dictionary, len(listA) + 1, len(listB) + 1)
