T = int(input()) #색종이의 수
arr = [[0] * 100 for _ in range(100)]
for tc in range(1, T+1):
    x1, y1 = map(int, input().split())
    x2, y2 = x1 + 10 , y1 + 10
    for i in range (x1, x2):
        for j in range(y1, y2):
            arr[i][j] += 1
cnt = 0
for k in range(100):
    for a in range(100):
        if arr[k][a] >= 1 :
            cnt += 1
print(cnt)