dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
def bfs(i, j):
    arr[i][j] = 0
    queue = [[i, j]]
    while queue:
        a, b = queue[0][0], queue[0][1] #i와 j
        queue.pop(0)
        for k in range(8): #방향
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < h and 0 <= y < w and arr[x][y] == 1:
                arr[x][y] = 0
                queue.append([x, y])
                
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = []
    count = 0
    for i in range(h):
        arr.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)