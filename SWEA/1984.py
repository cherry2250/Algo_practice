T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 0
    cnt = 0
    for i in arr[1:9]:
        ans += i
        cnt += 1
    s = round(ans/cnt)
    print(f'#{tc} {s}')