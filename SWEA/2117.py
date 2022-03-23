T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    K = 1 #앞으로 계속 증가하면서 값 비교
    while K <= (N//2)*2+1: #중앙을 중심으로 가득 채웠을 때까지
        cost = K*K +(K-1)*(K-1) #운영비용
        for j in range(N):
            for i in range(N):
                pro = 0
                cnt = 0
                for y in range(-K+1, K):
                    for x in range(-K+1, K):
                        if i+x>=0 and j+y>=0 and i+x<N and j+y<N:
                            if abs(x)+abs(y) <= K-1 and arr[j+y][i+x] == 1:
                                pro += M
                                cnt += 1
                benefit = pro - cost
                if benefit >= 0:
                    if cnt > max_cnt:
                        max_cnt = cnt
        K += 1
    print(f'#{tc} {max_cnt}')