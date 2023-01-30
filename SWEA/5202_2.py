T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    arr2 = sorted(arr, key=lambda x: x[1])

    cnt = 0
    now = 0

    for i in range(N):
        start = arr2[i][0]
        end = arr2[i][1]

        if now <= start:
            cnt += 1
            now = end

    print("#{} {}".format(tc, cnt))