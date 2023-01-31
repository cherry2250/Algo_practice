import sys
input = sys.stdin.readline

T = int(input())
arr = [list(map(str, input().split())) for _ in range(T)]
ans = sorted(arr, key=lambda x: (x[0]))
for i in range(len(ans)):
    print(ans[i][0], ans[i][1])