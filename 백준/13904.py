#처음 접근
# import sys
# input = sys.stdin.readline

# n = int(input())
# score = [list(map(int, input().split())) for _ in range(n)]
# score.sort(key=lambda x: (x[0], -x[1])) #마감 짧은것, 점수 높은 것 우선 정렬

# while score:
#     today = score[0][1]
#     for i in range(len(score)):
#         if score[i+1][0] == score[i][0] :


import sys
input = sys.stdin.readline

n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]
score.sort(key=lambda x: x[1], reverse=True)

date = [0] * 1001

for i in range(len(score)):
    if date[score[i][0]] == 0:
        date[score[i][0]] = score[i][1]
    else :
        if date[score[i][0]] < score[i][1]:
            date[score[i][[0]]] = score[i][1]

print(sum(date))
