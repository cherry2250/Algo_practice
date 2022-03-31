import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
num = int(input())
mid_num = num // len(arr)
ans = 0
cnt = 0
if sum(arr) <= num :
    print(max(arr))
else:
    for i in arr:
        if i < mid_num :
            ans += (mid_num - i)
            cnt += 1

    print(mid_num + (ans // (len(arr) - cnt)))