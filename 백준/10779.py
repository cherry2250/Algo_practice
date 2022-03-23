#쇠막대기
arr = list(input())
cnt = 0
ans = []
for i in range(len(arr)):
    if arr[i] == '(':
        ans.append(i)
    else: #')'인 경우
        if arr[i-1] == '(': #()인 경우
            ans.pop()
            cnt += len(ans)
        else :
            ans.pop()
            cnt += 1
print(cnt)