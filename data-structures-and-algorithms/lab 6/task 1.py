import sys  # provides get size of function

n = 26
data = []
for i in range(n):
    data.append(i)

for i in range(n):
    a = len(data)  # number of elements
    b = sys.getsizeof(data)  # actual size in bytes
    print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
    data.pop()
