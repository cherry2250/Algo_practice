import itertools


n, k = map(int, input().split())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)
ans = []
for i in range(1, n+1):
    ans.append(list(itertools.combinations(arr,i)))
print(ans)