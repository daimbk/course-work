# Lab 12
# Daim Bin Khalid
# 251686775

# Question 1

from functools import reduce

num = int(input('Enter number to get Fibonacci series up to: '))
result = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
print(result(num))
print()


# Question 2

fact_num = int(input('Enter number to find its factorial: '))

result = reduce(lambda x, y:  x * y, range(1, fact_num + 1))
print(result)
print()


# Question 3

num = int(input('Enter number to get Fibonacci series squared up to: '))
result = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
fibonacci_list = result(num)

fibonacci_squared = list(map(lambda x: x ** 2, fibonacci_list))
print(fibonacci_squared)
print()


# Question 4

vowels = ['a', 'e', 'i', 'o', 'u']
new_string = input('Enter string to filter out vowels in it: ')
result = list(filter(lambda x:  x not in vowels, new_string))
print(result)
print()
