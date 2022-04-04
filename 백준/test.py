# 이차원 배열을 순열 돌리는 법


n = [[1,2,3],
     [1,2,3],
     [1,2,3]]

행길이 = 3
열길이 = 4

좌표 = []

for i in range(행길이):
    for j in range(열길이):
        좌표.append( (i,j) )

print(좌표)

def check(i):
    if i == n:   # 갯수가 구하려는 순열 갯수와 같을때 까지 반복
        print(*case)

    for num in range(n):
        if not visited[num]:
            visited[num] = 1
            case[i] = 좌표[num]
            check(i+1)
            visited[num] = 0


n = int(input())
case = [0] * n
visited = [0] * (n + 1)
check(0)