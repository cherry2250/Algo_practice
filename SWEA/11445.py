T = int(input())
for i in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for j in reversed(range(0, N)):
        if a[N-1] > a[j] :
            ans += a[N-1] - a[j] 
        else :
            a[N-1] = a[j]
    print(f'#{i} {ans}')