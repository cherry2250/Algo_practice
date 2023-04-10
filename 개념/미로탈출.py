from collections import deque

n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int,input())))

# 방문 기록용
check = [[0]*m for _ in range(n)]
# 이동칸 기록용 
count = [[0]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0,0))
    # 시작 위치 방문 기록
    check[0][0] = 1
    # 시작 위치 이동칸 수 기록
    count[0][0] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 인접한 노드가 미로 내부에 존재하는지 확인
            if (nx >=0 and nx < n and ny >= 0 and ny < m):
                # 인접한 노드를 방문할 수 있는지 확인
                if (check[nx][ny] == 0 and maze[nx][ny] == 1):
                    # 방문할 수 있다면 큐에 삽입
                    queue.append((nx,ny))
                    # 인접 노드 방문 기록
                    check[nx][ny] = 1
                    # 인접 노드 이동칸 수 기록
                    count[nx][ny] = count[x][y] + 1

    return count[n-1][m-1]

print(bfs())