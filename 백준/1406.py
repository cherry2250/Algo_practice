#에디터
from sys import stdin
input = stdin.readline

arr_1 = list(input().strip())
T = int(input())
arr_2 = []
for tc in range(1,T+1):
    case = input().split()
    if case[0] == 'L':
        if not arr_1 :
            continue
        else:
            arr_2.append(arr_1[-1])
            arr_1.pop()
    elif case[0] == 'D':
        if not arr_2 :
            continue
        else:
            arr_1.append(arr_2[-1])
            arr_2.pop()
    elif case[0] == 'B':
        if not arr_1 :
            continue
        else:
            arr_1.pop()
    elif case[0] == 'P':
        arr_1.append(case[1])

n = len(arr_2)
for i in range(1, n+1):
    arr_1.append(arr_2[-i])

print(''.join(arr_1))