# approach is exactly the same as iterative 2d matrix as same data structure implementation and functions are used
# space complexity: O(rows * cols)

def test_display(text, matrix):
    print(text)
    for row in matrix:
        print(" ".join(f"{element:2}" for element in row))


def edit_distance_recursive(row, col, matrix, listA, listB):
    if matrix[row][col] == -1:
        if matrix[row - 1][col] == -1:
            costDel = edit_distance_recursive(
                row - 1, col, matrix, listA, listB) + 1
        else:
            costDel = matrix[row - 1][col] + 1

        if matrix[row][col - 1] == -1:
            costInsert = edit_distance_recursive(
                row, col - 1, matrix, listA, listB) + 1
        else:
            costInsert = matrix[row][col - 1] + 1

        if matrix[row - 1][col - 1] == -1 and listA[row - 1] == listB[col - 1]:
            cost = edit_distance_recursive(
                row - 1, col - 1, matrix, listA, listB)
        elif matrix[row - 1][col - 1] == -1 and listA[row - 1] != listB[col - 1]:
            cost = edit_distance_recursive(
                row - 1, col - 1, matrix, listA, listB) + 1
        elif matrix[row - 1][col - 1] != -1 and listA[row - 1] == listB[col - 1]:
            cost = matrix[row - 1][col - 1]
        elif matrix[row - 1][col - 1] != -1 and listA[row - 1] != listB[col - 1]:
            cost = matrix[row - 1][col - 1] + 1

        matrix[row][col] = min(costDel, costInsert, cost)

    return matrix[row][col]


# ----------------------test 1---------------------
listA = ["M", "A", "T", "H", "S"]
listB = ["A", "R", "T", "S"]

# declare 2d matrix
row = len(listA) + 1
col = len(listB) + 1
matrix = [[-1 for _ in range(col)] for _ in range(row)]

# filling of base rows
counter = 0
for j in range(col):
    matrix[0][j] = counter
    counter += 1

# filling of base cols
counter = 0
for i in range(row):
    matrix[i][0] = counter
    counter += 1

print("TEST 1")
print(f"Word 1 : {listA}\nWord 2 : {listB}")
test_display("BEFORE", matrix)
edit_distance_recursive(row - 1, col - 1, matrix, listA, listB)
test_display("\nAFTER", matrix)


# ----------------------test 2---------------------
listA = ["S", "I", "T", "T", "I", "N", "G"]
listB = ["K", "I", "T", "T", "E", "N"]

# declare 2d matrix
row = len(listA) + 1
col = len(listB) + 1
matrix = [[-1 for _ in range(col)] for _ in range(row)]

# filling of base rows
counter = 0
for j in range(col):
    matrix[0][j] = counter
    counter += 1

# filling of base cols
counter = 0
for i in range(row):
    matrix[i][0] = counter
    counter += 1

print("\nTEST 2")
print(f"Word 1 : {listA}\nWord 2 : {listB}")
test_display("BEFORE", matrix)
edit_distance_recursive(row - 1, col - 1, matrix, listA, listB)
test_display("\nAFTER", matrix)


# ----------------------test 3---------------------
listA = ["C", "O", "D", "I", "N", "G"]
listB = ["L", "A", "N", "G", "U", "A", "G", "E"]

# declare 2d matrix
row = len(listA) + 1
col = len(listB) + 1
matrix = [[-1 for _ in range(col)] for _ in range(row)]

# filling of base rows
counter = 0
for j in range(col):
    matrix[0][j] = counter
    counter += 1

# filling of base cols
counter = 0
for i in range(row):
    matrix[i][0] = counter
    counter += 1

print("\nTEST 3")
print(f"Word 1 : {listA}\nWord 2 : {listB}")
test_display("BEFORE", matrix)
edit_distance_recursive(row - 1, col - 1, matrix, listA, listB)
test_display("\nAFTER", matrix)
