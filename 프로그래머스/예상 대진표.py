def solution(n):
    dir = [(1, 0), (0, 1), (-1, -1)] #아래, 오른쪽, 좌상향 대각선
    
    arr = [[0] * i for i in range(1, n+1)]
    max_val = (n ** 2 + n) // 2 #달팽이에 들 어갈 숫자
    cnt = 0 #채운 숫자
    x, y = 0, 0 #초기값
    num = 0 #방향 전환 횟수
    
    while cnt < max_val: #while문 돌면서 1개씩 채움
        cnt += 1 
        arr[x][y] = cnt #값 넣음
        dx = x + dir[num][0] 
        dy = y + dir[num][1]
        if 0 <= dx < n and 0 <= dy < len(arr[dx]) and arr[dx][dy] == 0:
            x, y = dx, dy
        else:
            num = (num + 1) % 3 #방향 전환함
            x = x + dir[num][0]
            y = y + dir[num][1]

    answer = []
    for i in arr:
        answer.extend(i)
    return answer