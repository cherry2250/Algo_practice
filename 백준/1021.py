from collections import deque
import sys 
input = sys.stdin.readline 

N, M = map(int, input().split())
arr = list(map(int, input().split()))
que = deque([])
for i in range(1, N+1):
    que.append(i)
cnt = 0
while arr:
    if que[0] == arr[0]:
        que.popleft()
        arr.pop(0)
    else:
        if que.index(arr[0]) > len(que) / 2 : #3번이 빠를 때
            while que[0] != arr[0]:
                que.appendleft(que.pop())
                cnt += 1
        else:                                  #2번이 빠를 때
            while que[0] != arr[0]: 
                que.append(que.popleft())
                cnt += 1
print(cnt)