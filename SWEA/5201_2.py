T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)
    ans = 0
    now = 0
    for i in range(len(truck)):
        while container :
            if truck[i] >= container[0] :
                ans += container[0]
                container.pop(0)
                break
            else:
                container.pop(0)

    print(f'#{tc} {ans}')
