from collections import deque
import math

#4방향 지정
directions = [[1,0],[-1,0],[0,1],[0,-1]]
def solution(board):
    #x, y, cost, direction
    def bfs (i,j,c,d) :
        n = len(board)
        result = [ [math.inf for _ in range(n)] for _ in range(n)]
        # [[inf], [inf], [inf], [inf]] , [[inf], [inf], [inf], [inf]], [[inf], [inf], [inf], [inf]], [[inf], [inf], [inf], [inf]]
        queue = deque()
        queue.append((i,j,c,d))
        result[i][j] = 0
        while queue :
            x, y, cost, direction = queue.popleft()
            
            for i in range(4) :
                nx = x + directions[i][0]
                ny = y + directions[i][1]
                if direction == i :
                    ncost = cost + 100
                else :
                    cost + 600
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and result[nx][ny] > ncost :
                    result[nx][ny] = ncost
                    queue.append((nx,ny,ncost,i))
        return result[-1][-1]
    return min(bfs(0,0,0,0), bfs(0,0,0,2))