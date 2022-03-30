import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))
cnt = 0
res = []
for i in range(N):
    cnt += arr[i]
    res.append(cnt)
print(sum(res))