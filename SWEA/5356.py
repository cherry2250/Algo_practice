T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(5)]
    a = []
    for i in range(5):
        for j in range(5):
            a.append(i[j])