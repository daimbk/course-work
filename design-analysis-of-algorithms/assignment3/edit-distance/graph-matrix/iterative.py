# approach is exactly the same as iterative 2d matrix as same data structure implementation and functions are used
# space complexity: O(rows * cols)

def test_display(text, matrix):
    print(text)
    for row in matrix:
        print(" ".join(f"{element:2}" for element in row))


listA = ["M", "A", "T", "H", "S"]
listB = ["A", "R", "T", "S"]

# create graph adjacency matrix
rows = len(listA) + 1
cols = len(listB) + 1
matrix = [[-1 for j in range(cols)] for i in range(rows)]

# filling of base rows
counter = 0
for j in range(cols):
    matrix[0][j] = counter
    counter += 1

# filling of base cols
counter = 0
for i in range(rows):
    matrix[i][0] = counter
    counter += 1

test_display("BEFORE", matrix)


def edit_distance_iterative(matrix, listA, listB):
    for row in range(1, rows):
        for col in range(1, cols):
            if matrix[row][col] == -1:
                costDel = matrix[row - 1][col] + 1
                costInsert = matrix[row][col - 1] + 1
                costReplace = matrix[row - 1][col - 1] + \
                    (0 if listA[row - 1] == listB[col - 1] else 1)
                matrix[row][col] = min(costDel, costInsert, costReplace)


edit_distance_iterative(matrix, listA, listB)
test_display("\nAFTER", matrix)
