T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) #숫자, K의 위치
    score = []
    for i in range(N+1):
        m, f, h = map(int, input().split()) #middle final homework
        score.append(m*0.35 + f*0.45 + h*0.2)
    a = score[K-1]
    score.sort()
    b = score.index(a)
    
    GPA = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    print(f'#{tc} {GPA[b//(N//10)]}')