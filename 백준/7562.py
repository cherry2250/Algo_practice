from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(now_x, now_y):
    q = deque()
    q.append([now_x, now_y])
    arr[now_x][now_y] = 1
    while q:
        a, b = q.popleft()
        
        if a == p_x and b == p_y:
            break
        
        #방향탐색
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 0:
                    q.append([nx, ny])
                    arr[nx][ny] = arr[a][b] + 1
    return graph                
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = []
    for i in range(N):
        graph.append([0] * N)
    now_x, now_y = map(int, input().split())
    p_x, p_y = map(int, input().split())
    arr = [[0] * N for i in range(N)]
    
    print( bfs(now_x, now_y) )