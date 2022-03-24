T = int(input())
for tc in range(1, T+1):
    num = float(input())
    result = ''
    i = 1
    while True:
        num *= 2
        if num == 1:
            result += '1'
            print(f'#{tc} {result}')
            break
        elif num > 1:
            num -= 1
            result += '1'
        else :
            result += '0'
            
        if i >= 13:
            print(f'#{tc} overflow')
            break
        i += 1