# Lab 9.          Name: Daim Bin Khalid.      Roll no.: 251686775

# Task 1

nat_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda i: i % 2 == 0, nat_list))
odd_list = list(filter(lambda i: i % 2 != 0, nat_list))
print(even_list,'\n',odd_list, sep ='')


# Task 2

even_list = list(map(lambda i: i % 2 == 0, nat_list))
odd_list = list(map(lambda i: i % 2 != 0, nat_list))
print(even_list,'\n',odd_list, sep = '')


# Task 3

a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]

common = list(filter(lambda i: (i in a and b), b))
print(common)


# Task 4

common_list = [i for i in b if i in a and b]
print(common_list)