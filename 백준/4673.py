import sys
import copy 
input = sys.stdin.readline

T = int(input())
arr = []
for tc in range(1, T+1):
    A, B = map(int, input().split())
    arr.append([A, B, tc, 0])

arr.sort(key=lambda x : -x[0])

now = 1
for i in range(1, len(arr)):
    if arr[i-1][0] > arr[i][0] and arr[i-1][1] > arr[i][1]:
        if now == 1 :
            now = 1
        else : 
            now = i+1
        arr[i-1][3] = now
        now += 1

    else : 
        arr[i-1][3] = now

arr[len(arr)-1][3] = now

arr.sort(key=lambda x : x[2])
ans = []
for j in range(len(arr)) :
    ans.append(arr[j][3])
print(arr)
print(' '.join(map(str, ans)))