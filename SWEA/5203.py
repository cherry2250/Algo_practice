T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    v1 = [0] * 10
    v2 = [0] * 10
    res = 0
    for i in range(len(arr)):
        if res != 0:
            break
        if i % 2 == 0 :
            v1[arr[i]] += 1
            if v1[arr[i]] >= 3:
                res = 1
            elif v1[arr[i]-1] >= 1 and v1[arr[i]] >= 1 and v1[arr[i]+1] >= 1:
                res = 1
        if i % 2 == 1 :
            v2[arr[i]] += 1
            if v2[arr[i]] >= 3:
                res = 2
            elif v2[arr[i]-1] >= 1 and v2[arr[i]] >= 1 and v2[arr[i]+1] >= 1:
                res = 2
    print(f'#{tc} {res}')