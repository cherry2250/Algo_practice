import sys
input = sys.stdin.readline

T = int(input())
arr = []
for tc in range(1, T+1):
    data = int(input())
    if data == 0:
        arr.pop()
    else:
        arr.append(data)
print(sum(arr))