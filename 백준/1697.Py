import sys
from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        #동생이랑 위치 같아질 때
        if v == k:
            return visited[v]
        for now in (v-1, v+1, 2*v): #문제 조건 : 이동 or 순간이동
            #범위 내에 있고, 아직 미방문
            if 0 <= now < MAX and not visited[now]:
                visited[now] = visited[v] + 1
                q.append(now)


MAX = 100001
n, k = map(int, sys.stdin.readline().split())
visited = [0] * MAX #방문체크
print(bfs(n))