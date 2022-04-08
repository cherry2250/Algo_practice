import sys
input = sys.stdin.readline

n, t = map(int, input().split())
arr = [0] + list(map(int, input().split()))
for tc in range(1, t+1):
    i, j = map(int, input().split())
    print(sum(arr[i:j+1]))