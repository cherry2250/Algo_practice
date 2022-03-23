T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    ans = []
    for i in range(len(arr)):
        if arr[i] == '(':
            ans.append(arr[i])
        else:
            if len(ans) > 0 and ans[-1] == '(':
                ans.pop()
            else:
                ans.append('X')
                break
            
    if len(ans) != 0 :
        print('NO')
    else:
        print('YES')