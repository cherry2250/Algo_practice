T = int(input())
for tc in range(1, T+1):
    k = int(input())
    n = int(input())
    peo = []
    for i in range(1, n+1):
        peo.append(i)
    for _ in range(k):
        for j in range(1, n):
            peo[j] += peo[j-1]
    print(peo[-1])