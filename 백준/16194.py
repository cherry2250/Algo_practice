import sys
input = sys.stdin.readline

T = int(input())
arr = [0] + list(map(int,input().split()))
dp = [0] + [10001]*(T+1)

for i in range(1, T+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i],arr[j]+dp[i-j])
print(dp[T])