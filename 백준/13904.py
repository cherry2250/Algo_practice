# #처음 접근
# import sys
# input = sys.stdin.readline

# n = int(input())
# score = [list(map(int, input().split())) for _ in range(n)]
# score.sort(key=lambda x: (x[0], -x[1])) #마감 짧은것, 점수 높은 것 우선 정렬

# while score:
#     today = score[0][1]
#     for i in range(len(score)):
#         if score[i+1][0] == score[i][0] :

# #다음 접근 -> 마감 기한에 딱 맞게 제출하기
# import sys
# input = sys.stdin.readline

# n = int(input())
# score = [list(map(int, input().split())) for _ in range(n)]
# score.sort(key=lambda x: x[1], reverse=True)

# date = [0] * 1001

# for i in range(len(score)):
#     if date[score[i][0]] == 0:
#         date[score[i][0]] = score[i][1]
#     else :
#         if date[score[i][0]] < score[i][1]:
#             date[score[i][[0]]] = score[i][1]

# print(sum(date))


#정답 코드
import sys
N = int(sys.stdin.readline())
homeworks = []
visit = [False] * 1001

for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())
    homeworks.append((d, w))

homeworks.sort(key=lambda x: x[1], reverse=True)
answer = 0
for day, worth in homeworks:
    i = day
    # 과제를 할 날짜 탐색
    while i > 0 and visit[i]:
        i -= 1
    # 과제를 할 날짜가 없으면 패스
    if i == 0:
        continue
    else:
        visit[i] = True
        answer += worth

print(answer)