def BFS(x, y):
    global min_a, sum_a
    # 더 계산할 필요가 없다.
    if min_a < sum_a:
        return
    # x,y가 N-1, N-1 즉 목적지에 도달하면 종료
    if x == N-1 and y == N-1:
        if min_a > sum_a:
            min_a = sum_a
    # 아래, 오른쪽으로만 진행 가능
    dx = [1,0] 
    dy = [0,1]
    for i in range(2):
        di = x+dx[i]
        dj = y+dy[i]
        if 0 <= di < N and 0 <= dj <N and not visited[di][dj]:
            visited[di][dj] = True
            sum_a += arr[di][dj]
            BFS(di,dj)
            visited[di][dj] = False
            sum_a -= arr[di][dj]
 
# testcase 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # N의 최대값은 13이고 10 이하의 자연수 이므로 합이 260을 넘을 수 없다.
    min_a = 987654321
    # 부분합 계산
    sum_a = arr[0][0]
    # 방문한 위치 체크
    visited = [[False for _ in range(N)] for i in range(N)]
    # 0,0에서 출발
    BFS(0,0)
    print(f"#{tc} {min_a}")