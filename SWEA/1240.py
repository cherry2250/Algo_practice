num = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6, 
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9 }
T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    arr = [input() for _ in range(N)]
    find = False
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                r_idx = i
                c_idx = j
                find = True
                break
        if find:
            break
    password = arr[r_idx][c_idx-55 : c_idx+1]
    a, b = 0, 0
    for k in range(7):
        if k % 2 == 0:
            a += num[password[7*k : 7*(k + 1)]]
        else:
            b += num[password[7*k : 7*(k + 1)]]
    result = a*3 + b
    if (result + num[password[-7:]]) % 10 != 0:
        result = 0
    else:
        result = a + b + num[password[-7:]]
    print(f'#{tc} {result}')