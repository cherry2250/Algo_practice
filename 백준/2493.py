#탑
from sys import stdin
input = stdin.readline

T = int(input())
arr = list(map(int, input().split()))
arr_1 = arr.reverse()
stack = []
ans = [0]*T
for i in range(len(arr)):
    while stack and arr[stack[-1]] < arr[i]: 
        ans[stack[-1]] = i
        stack.pop()
    stack.append(i)
for i in range(len(ans)):
    if ans[i] == 0:
        pass
    else:
        ans[i] = len(ans) - ans[i]
ans.reverse()
print(*ans)