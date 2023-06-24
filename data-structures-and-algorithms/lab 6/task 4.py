two_dim_list = [[1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]

total = 0
for lists in two_dim_list:
    for internal_list in lists:
        total += internal_list

print(f'Total without comprehension method: {total}')

total = sum([i for lists in two_dim_list for i in lists])
print(f'Total with list comprehension: {total}')
