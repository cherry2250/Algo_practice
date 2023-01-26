import sys

W, N = map(int, input().split())
ans = 0
arr = []
for tc in range(1, N+1):
    M, P = map(int, input().split())
    arr.append([P, M])
    arr.sort(reverse=True)

while W >= 0 :
    if W == 0 :
        break
    if arr[0][1] <= W :
        ans += arr[0][1] * arr[0][0]
        W -= arr[0][1]
        arr.pop(0)
    else :
        ans += W * arr[0][0]
        W = 0

print(ans)