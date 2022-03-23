def check():  
    for i in range(9):
        cnt = [0] * 10
        for c in range(9):
            t = arr[i][c]
            if cnt[t] == 1:
                return 0
            cnt[t] = 1
 
 
        cnt = [0] * 10
        for r in range(9):
            t = arr[r][i]
            if cnt[t] == 1:
                return 0
            cnt[t] = 1
 
    for str in range(0, 9, 3):
        for stc in range(0, 9, 3):
            cnt = [0] * 10
            for r in range(3):
                for c in range(3):
                    t = arr[str+r][stc+c]
                    if cnt[t] == 1:
                        return 0
                    cnt[t] = 1
    return 1
 
T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)] 
    print(f'#{tc} {check()}')