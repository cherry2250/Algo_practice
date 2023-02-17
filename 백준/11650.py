import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    A, B = map(int, input().split())
    s = (A, B)
    arr.append(s)
arr.sort()
for i in range(n):
    print(*arr[i])