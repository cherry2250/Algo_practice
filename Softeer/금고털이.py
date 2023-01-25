import sys

W, N = map(int, sys.stdin.readline().split())
ans = 0
arr = [list(map(int, sys.stdin.readline().split())) for x in range(N)]
arr.sort(key=lambda x :-x[1])

for i in range(N):
    if arr[i][0] <= W :
        ans += arr[i][1] * arr[i][0]
        W -= arr[i][0]
    else :
        ans += W * arr[i][1]
        break

print(ans)