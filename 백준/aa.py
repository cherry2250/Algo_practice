from collections import deque
import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(a, b):
    queue = deque()
    queue.append([a,b])
    graph[a][b] = 0
    count = 1
    while queue:
        x, y = queue.popleft()
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append([nx, ny])
                    count += 1
    return count
N = int(input())
graph = []
res = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count = bfs(i, j)
            res.append(count)
res.sort