import sys 
input = sys.stdin.readline 

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.reverse()
 
dp = [0]*N
dp[0] = arr[0]

for i in range(1, N):
    if i < 3:
        dp[i] = arr[0] + arr[i]
    else:
        dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])

print(max(dp[N-2], dp[N-1]))