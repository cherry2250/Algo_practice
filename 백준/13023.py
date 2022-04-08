import sys
input = sys.stdin.readline

def dfs(v,d):
    if d==4:
        print(1)
        sys.exit() # 전체 끝내버리기
    for i in arr[v]:
        if visit[i] == 0:
            visit[i] = 1
            dfs(i,d+1)
            visit[i] = 0


n, m = map(int,input().split())
arr = [[] for _ in range(n)]
visit = [0] * n

for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

for start in range(n):
    visit[start] = 1
    dfs(start,0)
    visit[start] = 0
    
print(0)