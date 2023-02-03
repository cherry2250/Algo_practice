alpha = ['=c', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
check = list(input())
cnt = 0
while check :
    for i in range(len(check) -1):
        if check[i] == 'd' and check[i+1] =='z':
            if i <= len(check) -2 and check[i+2] == '=':
                cnt += 1
                check.pop(0)
                check.pop(0)
                check.pop(0)
                break
        elif check[i] + check[i+1] in alpha :
            check.pop(0)
            check.pop(0)
            cnt += 1
            break
        else :
            cnt += 1
            check.pop(0)
            break
    if len(check) == 1 :
        cnt += 1
        check.pop(0)

print(cnt)