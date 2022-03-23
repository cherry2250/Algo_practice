# 스택수열
import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
ans = []
stack = []
wrong = 0
for i in range(0, N):
    num = int(input())
    while cnt < num:
        cnt += 1
        stack.append(cnt)
        ans.append('+')
            
    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    else:
        wrong = 1
        break
if wrong == 1:
    print("NO")
else : 
    print("\n".join(ans))