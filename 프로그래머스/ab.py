def solution(n,m,x,y,z):
    INF = int(1e9)
    visited = [False] * (n+1)
    graph = [[] for i in range(n+1)]
    
    ans = sorted(z)
    print(ans)
    answer = []
    a = 1
    for i in range(n):
        for j in range(n):
            if ans[i] == z[j]:
                answer.append(j+a)
                
    print(answer) 
    

solution(4, 4, [1, 1, 3, 4], [3, 4, 2, 2], [2, 1, 1, 2])