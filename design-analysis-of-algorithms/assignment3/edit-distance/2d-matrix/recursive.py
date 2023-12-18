# approach is the same as graph adjacency matrix
# space complexity: O(rows * cols)

def test_display(text, matrix):
    print(text)
    for row in matrix:
        print(" ".join(f"{element:2}" for element in row))


listA = ["M", "A", "T", "H", "S"]
listB = ["A", "R", "T", "S"]

# declare 2d matrix
row = len(listA) + 1
col = len(listB) + 1
matrix = [[-1 for j in range(col)] for i in range(row)]

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


test_display("BEFORE", matrix)


def edit_distance_recursive(row, col, matrix, listA, listB):
    if (matrix[row][col] == -1):
        if (matrix[row - 1][col] == -1):
            costDel = edit_distance_recursive(
                row - 1, col, matrix, listA, listB) + 1
        else:
            costDel = matrix[row - 1][col] + 1

        if (matrix[row][col-1] == -1):
            costInsert = edit_distance_recursive(
                row, col - 1, matrix, listA, listB) + 1
        else:
            costInsert = matrix[row][col - 1] + 1

        if (matrix[row - 1][col - 1] == -1 and listA[row - 1] == listB[col - 1]):
            cost = edit_distance_recursive(
                row - 1, col - 1, matrix, listA, listB)

        elif (matrix[row - 1][col - 1] == -1 and listA[row - 1] != listB[col - 1]):
            cost = edit_distance_recursive(
                row - 1, col - 1, matrix, listA, listB) + 1

        elif (matrix[row - 1][col - 1] != -1 and listA[row - 1] == listB[col - 1]):
            cost = matrix[row - 1][col - 1]

        elif (matrix[row - 1][col - 1] != -1 and listA[row - 1] != listB[col - 1]):
            cost = matrix[row - 1][col - 1] + 1

        matrix[row][col] = min(costDel, costInsert, cost)

    return matrix[row][col]


edit_distance_recursive(row - 1, col - 1, matrix, listA, listB)
test_display("\nAFTER", matrix)
