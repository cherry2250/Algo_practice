from sys import stdin
input = stdin.readline
arr = list(map(int, input().split()))
A = arr[0]
B = arr[1]-1
print(A*B +1)
