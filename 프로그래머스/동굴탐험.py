def dfs(node):
    stack = [node]
    visited[node] = True
    while stack:
        curr = stack.pop() #curr = 현재 노드
        for next in graph[curr]:
            if n_visit[curr]: #후 방문이 있을 경우 점프
                dfs(n_visit[curr])
            if not visited[p_visit[curr]]: #먼저 방문해야할 노드를 방문하지 않았을 경우
                n_visit[p_visit[curr]] = curr #후 방문 list에 저장
                continue
            if not visited[next]: #방문한 적 없는 노드일경우 stack에 추가
                stack.append(next)
                visited[next] = True
 
def solution(n, path, order):
    global graph, p_visit, n_visit, visited
    graph = [[] for _ in range(n)]
    p_visit = [0 for _ in range(n)]
    n_visit = [0 for _ in range(n)]
    visited = [False for _ in range(n)]
    
    #양방향 그래프 생성
    for p in path:
        graph[p[0]].append(p[1])
        graph[p[1]].append(p[0])
        
    #order 적용
    for p in order:
        p_visit[p[1]] = p[0]
        
    dfs(0) #dfs 실행
    
    if sum(visited) == n: #모두 방문했을 경우 True 출력
        return True
    
    return False