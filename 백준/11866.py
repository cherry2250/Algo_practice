from collections import deque
import sys 
input = sys.stdin.readline 

N, K = map(int, input().split())
que = deque([])
ans = []
for i in range(1, N+1):
    que.append(i)
#원형 큐
index = 0    
while len(que) >= 1:
    if index + 1 == K : 
        ans.append(que.popleft())
        index = 0
    else :
        que.append(que.popleft())
        index += 1
print(f'<', end='')
print(*ans, sep=', ', end='')
print(f'>')