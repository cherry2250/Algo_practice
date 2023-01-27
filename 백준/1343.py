arr=list(map(str, input()))
ans = ''
while arr and ans != '-1':
    if arr[0] == 'X':
        temp = 0
        for i in range(len(arr)):
            if arr[i] == 'X':
                temp += 1
            elif arr[i] == '.':
                break
        if temp % 4 == 0 :
            now = temp // 4
            ans += ('AAAA' * now)
        elif temp % 4 == 2:
            now = temp // 4
            if now != 0 :
                ans += ('AAAA'*now)
                ans += 'BB'
            else :
                ans += 'BB'
        else :
            ans = '-1'
            break
        del arr[:temp]
    elif arr[0] == '.':
        ans += arr[0]
        arr.pop(0)

print(ans)