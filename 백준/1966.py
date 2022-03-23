import sys 
input = sys.stdin.readline 

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    index = []
    for i in range(n):
        index.append(i)
    index[m] = 'a'
    cnt = 0
 
    while arr:
        if arr[0] == max(arr):
            cnt += 1
            if index[0] == 'a':
                print(cnt)
                break
            arr.pop(0)
            index.pop(0)
        else:
            arr.append(arr.pop(0))
            index.append(index.pop(0))