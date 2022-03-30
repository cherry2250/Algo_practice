import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

#노가다...
tetromino = [
    [(0, 0), (0, 1), (1, 0), (1, 1)], #정사각형
    [(0, 0), (0, 1), (0, 2), (0, 3)], #가로 일직선 
    [(0, 0), (1, 0), (2, 0), (3, 0)],  #세로 일직선
    [(0, 0), (1, 0), (1, 1), (2, 1)], #L 뒤집어 놓은 것
    [(0, 0), (1, 0), (1, -1), (2, -1)],  #가로 지그재그
    [(0, 0), (0, 1), (1, 1), (1, 2)],  #세로 지그재그
    [(0, 0), (0, 1), (-1, 1), (-1, 2)],  #f y축 대칭
    [(0, 0), (0, 1), (0, 2), (1, 2)],  #L 90도 회전
    [(0, 0), (1, 0), (2, 0), (2, -1)],  #ㄱ 모양
    [(0, 0), (1, 0), (1, 1), (1, 2)],  #L 180도 회전
    [(0, 0), (0, -1), (1, -1), (2, -1)],  #ㄴ 가로
    [(0, 0), (-1, 0), (-1, 1), (-1, 2)], #ㄴ 세로
    [(0, 0), (1, 0), (2, 0), (2, 1)],  #L 270도
    [(0, 0), (0, 1), (0, 2), (-1, 2)],  #ㄱ 세로
    [(0, 0), (0, 1), (1, 1), (2, 1)],  # ㄱ 가로 대칭
    [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
    [(1, 0), (1, 1), (1, 2), (0, 1)],  # ㅗ
    [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
    [(1, 0), (0, 1), (1, 1), (2, 1)],  # ㅓ
]


answer = 0
for i in range(n):
    for j in range(m):
        for k in range(len(tetromino)):
            result = 0
            for s in range(len(tetromino[k])):
                try :
                    next_x = i + tetromino[k][s][0]  # 인자의 x좌표만큼 테트로미노의 x 좌표를 옮겨준다.
                    next_y = j + tetromino[k][s][1]  # 인자의 y좌표만큼 테트로미노의 y 좌표를 옮겨준다.
                    result += arr[next_x][next_y] 
                except IndexError:  # indexError가발생하면
                    print(next_x, next_y, k, s)
                    break #반복문 탈출
            answer = max(answer, result)    
print(answer)    



# def find(x, y):
#     global answer
#     for i in range(len(tetromino)):  # 테트로 미노의 행의 길이만큼
#         result = 0
#         for j in range(len(tetromino[i])):  # 테트로 미노의 열의 길이만큼
#             try:
#                 next_x = x + tetromino[i][j][0]  # 인자의 x좌표만큼 테트로미노의 x 좌표를 옮겨준다.
#                 next_y = y + tetromino[i][j][1]  # 인자의 y좌표만큼 테트로미노의 y 좌표를 옮겨준다.
#                 result += arr[next_x][next_y]  # 입력받은 좌표의 테트로미노 좌표에 있는 숫자들을 계속더해준다.
#             except IndexError:  # indexError가발생하면
#                 break #반복문 탈출
#         answer = max(answer, result)  # result값의 최댓값을 계속해서 저장


# def solve():
#     for i in range(n):  # 입력받은 좌표의 행의개수 만큼
#         for j in range(m):  # 입력받은 좌표의 열의 개수 만큼
#             find(i, j)  # 함수실행


# answer = 0
# solve()
# print(answer)