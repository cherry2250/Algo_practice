import itertools
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

num = [2, 3, 4, 5, 6, 7, 8, 9] #1은 3번자리 고정
play = list(itertools.permutations(num, 8))

def baseball(i, arr):
    out = 0
    score = 0
    base1, base2, base3 = 0,0,0
    while True :
        if out == 3:
             break
        if arr[i] == 1:
            if base1 == 0:
                base1 += 1
            else : 
                base2 += 1
        if arr[i] == 2:
            if base2 == 0:
                base2 += 1
            else :
                base3 += 1
        if arr[i] == 3:
            if base3 == 0:
                base3 += 1
            else :
                score += 1
                
        #모르겠습니다..