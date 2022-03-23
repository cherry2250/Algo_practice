T = int(input())
for tc in range(1, T+1):
    node_num, line_num = map(int, input().split())
    arr = []
    for i in range(len(line_num)):
        S, E = map(int, input().split())
        arr.append([S, E])

    start, end = map(int, input().split())
    ans = [start]
    visit = [0] * (node_num +1)
    while ans :
        now = ans.pop()
        visit[now] = T
        for i in arr:
            if now == i[0]:
                if visit[i[1]] == 0 :
                    ans.append(i[1])
    if visit[end] : 
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')