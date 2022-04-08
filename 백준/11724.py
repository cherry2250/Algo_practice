import sys
input = sys.stdin.readline

def bfs(v):
    queue = [v]
    visit[v] = 1
    while queue:
        v = queue[0]
        queue.pop(0)
        for i in range(1, N+1):
            if visit[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visit[i] = 1


N, M = map(int, input().split())
graph = [[0] *(N+1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 방문처리
visit = [0] * (N + 1)
count = 0  # 컴포넌트 그래프 개수 저장

# 1~N번 노드를 각각돌면서
for i in range(1, N + 1):
    if visit[i] == 0:  # 만약 방문하지 않았다면
        if graph[i] == 0:  # 만약 그래프가 비어있다면
            count += 1  # 개수 1개 추가
            visit[i] = 1  # 방문 처리
        else:  # 만약 그래프가 비어있지 않다면(어느 점과 연결된 점이 있다면)
            bfs(i)  # 해당 i를 시작노드로 bfs를 돈다.
            count += 1  # 연결요소 를 +1개 해준다.
print(count)