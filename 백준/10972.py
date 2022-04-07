import itertools
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(1, n+1):
    arr.append(i)
find = list(map(int, input().split()))
per = list(itertools.permutations(arr, n))
for j in range(len(per)) :
    if j == len(per):
        print(-1)
    if tuple(find) == per[j]:
        for k in per[j+1]:
            print(k, end=' ')
    