import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)], reverse=True)
cnt = 0
for i in arr:
    if K // i != 0:
        cnt += (K//i)
        K = K % i
print(cnt)