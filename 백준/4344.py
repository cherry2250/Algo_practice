T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    ans = sum(arr) / N
    cnt = 0
    for i in arr :
        if i > ans:
            cnt += 1
    res = round((cnt / len(arr)) * 100, 3)
    print(f'{res:.3f}%')
