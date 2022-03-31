import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(0, N, 1):
    start, finish = input().split()
    arr.append((int(finish), int(start)))
arr.sort()
cnt = 1
last = arr[0][0]
for i in range(1, N):
    if last <= arr[i][1]:
        cnt += 1
        last = arr[i][0]
print(cnt)