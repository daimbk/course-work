# approach is the same as graph adjacency list
# space complexity: O(rows * cols)

def test_display(text, dictionary, rows, cols):
    print(text)
    for i in range(rows):
        row_values = " ".join(f"{dictionary[(i, j)]:2}" for j in range(cols))
        print(row_values)


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

test_display("BEFORE", dictionary, len(listA) + 1, len(listB) + 1)


def edit_distance_iterative(dictionary, listA, listB, rows, cols):
    for i in range(1, rows):
        for j in range(1, cols):
            if dictionary[(i, j)] == -1:
                costDel = dictionary[(i - 1, j)] + 1
                costInsert = dictionary[(i, j - 1)] + 1
                costReplace = dictionary[(i - 1, j - 1)] + \
                    (0 if listA[i - 1] == listB[j - 1] else 1)
                dictionary[(i, j)] = min(costDel, costInsert, costReplace)


edit_distance_iterative(dictionary, listA, listB,
                        len(listA) + 1, len(listB) + 1)
test_display("\nAFTER", dictionary, len(listA) + 1, len(listB) + 1)
