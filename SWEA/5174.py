T = int(input())
for tc in range(1, T+1):
    E, v = map(int, input().split())
    arr = list(map(int, input().split()))
    check = [0]
    for i in range(len(arr))