import sys
input = sys.stdin.readline

T = int(input())
arr = []
for tc in range(1, T+1):
    data = int(input())
    arr.append(data)

count = 0
max_V = 0
for i in range(1, T+1):
    if arr[-i] > max_V:
        count += 1
        max_V = arr[-i]
print(count)