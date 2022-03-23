from collections import deque
import sys 
input = sys.stdin.readline 

num = int(input())
que = deque([])
for i in range(1, num+1):
    que.append(i)

while len(que) > 1:
    que.popleft()
    que.append(que[0])
    que.popleft()

print(que[0])