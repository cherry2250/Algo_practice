T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    con = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)
    cnt = 0
    while con and truck:
        truck_n = truck.pop(0)
        while con:
            con_n = con.pop(0)
            if truck_n >= con_n:
                cnt += con_n
                break
    print(f'#{tc} {cnt}')