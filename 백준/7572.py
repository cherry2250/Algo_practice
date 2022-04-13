from collections import deque
import sys
input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():  
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append([nx, ny])

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append([i, j])
bfs()
res = 0
for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            sys.exit()
    res = max(res, max(i))
print(res -1)