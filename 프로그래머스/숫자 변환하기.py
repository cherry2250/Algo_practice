def solution(x, y, n):
    answer = 0
    INF = int(1e9)
    distance = [INF] * (y+1)
    distance[x] = 0

    for i in range(x+1, y+1) :
        distance[i] = min(distance[i//3]+1, distance[i//2]+1, distance[i-n]+1)
        if i % 3 == 0 and i % 2 == 0 :
            distance[i] = min(distance[i//3]+1, distance[i//2]+1, distance[i-n]+1)
        elif i % 3 == 0 :
            distance[i] = min(distance[i//3]+1, distance[i-n]+1)
        elif i % 2 == 0 :
            distance[i] = min(distance[i//2]+1, distance[i-n]+1)
        else :
            distance[i] = distance[i-n]+1
    if distance[y] >= INF :
        answer = -1
    else :
        answer = distance[y]

    return answer