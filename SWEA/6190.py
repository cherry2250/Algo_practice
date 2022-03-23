def check(value):
    strV = str(value)
    for i in range(1, len(strV)) :
        if strV[i-1] > strV[i]:
            return False
    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    maxV = -1
    for i in range(N):
        for j in range(i+1, N):
            value = arr[i] * arr[j]
            if check(value):
                if maxV < value :
                    maxV = value
    print(f'#{tc} {maxV}')    