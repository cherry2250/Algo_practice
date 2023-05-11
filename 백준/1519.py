n,m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
result = 0
 
def check_size(r,c):
    if 0<r<n and 0<c<m:
        left = int(dp[r][c-1])
        up = int(dp[r-1][c])
        left_diag = int(dp[r-1][c-1])
        return min(left, up, left_diag) + 1
    return 1
 
for r in range(n):
    for c in range(m):
        if arr[r][c]=='1':
            dp[r][c] = check_size(r,c)
            result = max(result, dp[r][c])
print(result**2)