import sys
input = sys.stdin.readline

S = list(input().strip())
T = list(input().strip())

while T:
    if T==S:
        print(1)
        sys.exit() #조건 부합 -> 프로그램 아예 종료해버림

    if T[-1]=='A': # 마지막이 A이면
        T.pop() #삭제
    elif T[-1]=='B': # 마지막이 B이면
        T.pop()
        T.reverse()
print(0)
