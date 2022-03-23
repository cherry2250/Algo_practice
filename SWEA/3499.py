T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr_a = arr[::N//2]
    arr_b = arr[N//2::]
    list_a = []
    for i in range(N//2):
        list_a.append(arr_a[i])
        list_a.append(arr_b[i])
    ans = ' '.join(list_a)
    print(f'#{tc} {ans}')