def perm(n, k, res):   # n:배열크기, k:깊이
    global min_a
    if k == N-1:
        res += arr[n][0]
        if res < min_a:
            min_a = res
    else:
        for i in range(1, N):
            if visited[i] == 0:
                visited[i] = 1
                perm(i, k+1, res+arr[n][i])
                visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    visited[0] = 1
    min_a = 987654321
    perm(0, 0, 0)
    print(f'#{tc} {min_a}')