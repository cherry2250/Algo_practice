from sys import stdin
input = stdin.readline

T = int(input())
for tc in range(1, T+1):
    arr = input().split()
    num = float(arr[0])
    N = len(arr)
    for i in range(1, N):
        if arr[i] == '@':
            num *= 3
        elif arr[i] == '%':
            num += 5
        elif arr[i] == '#':
            num -= 7
    print("%0.2f" % num)