T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                k = 1
            elif arr[i][j] == 'B':
                k = 2
            elif arr[i][j] == 'C':
                k = 3
                
            for a in range(1, k+1):
                #상
                if i-a >= 0 and arr[i-a][j] =='H':
                    arr[i-a][j] = '0'
                #하
                if i+a <= N-1 and arr[i+a][j] =='H':
                    arr[i+a][j] = '0'
                #좌
                if j-a >= 0 and arr[i][j-a] =='H':
                    arr[i][j-a] = '0'
                #우
                if j+a <= N-1 and arr[i][j+a] =='H':
                    arr[i][j+a] = '0'
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1
                
    print(f'#{tc} {cnt}') 
