import itertools
import sys
input = sys.stdin.readline

n = int(input())
num = []
for i in range(1, n+1):
    num.append(i)
arr = list(itertools.permutations(num))
for i in range(len(arr)):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()