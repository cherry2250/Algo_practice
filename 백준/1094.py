import itertools

n = int(input())
arr = [1, 1, 2, 4, 8, 16, 32, 64]
res = 0
b = []
for i in range(1, len(arr)+1):
    b += list(itertools.combinations(arr, i))
for i in range(len(b)):
    if n == sum(b[i]):
        print(len(b[i]))
        break