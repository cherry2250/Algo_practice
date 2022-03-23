def maze(y, x):
    global flag
    if arr[y][x] == 3:  # 도착하면
        flag = 1
        return
 
    arr[y][x] = 9  # 방문표시
 
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
 
        # 0:길, 1:벽, 2:출발점, 3:도착점, 9:방문
        if ny < 0 or ny == N: continue  # 인덱스 체크 (가장 먼저 해야 함)
        if nx < 0 or nx == N: continue
        if arr[ny][nx] == 9: 
            continue  # 방문 체크
        if arr[ny][nx] == 1: 
            continue  # 벽 체크
        maze(ny, nx)
 
 
def findStart(arr):
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                return y, x
 
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
T = int(input())
for tc in range(T):
    flag = 0
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    sy, sx = findStart(arr)
    maze(sy, sx)
    print("#{} {}".format(tc + 1, flag))