T = int(input())
for tc in range(1 , T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    
    arr.sort()
    a = "Possible"
    for i in range(N):
        t = arr[i]//M * K
        if t < (i+1):
            a = 'Impossible'
            break
    print(f'#{tc} {a}')