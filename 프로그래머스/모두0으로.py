from collections import deque

def find_tree(a, edges):
    
    dic = {}
    
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        
        if v1 not in dic.keys():
            dic[v1] = []
        if v2 not in dic.keys():
            dic[v2] = []
            
        dic[v1].append(v2)
        dic[v2].append(v1)
    
    # 바뀐 부분 : list 대신에 dequeue를 사용
    q = deque([(-1,0)])
    path = []
    visited = [0] * len(a)
    visited[0] = 1
        
    while q:
        p,c = q.popleft()
        path.append((p,c))
        
        des = dic[c]
        if des:
            for d in des:
                if not visited[d]:
                    q.append((c,d))
                    visited[d] = True
                    
    return path[::-1] 