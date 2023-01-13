N, M = map(int, input().split())
C = [int(input()) for i in range(N)]
dp = [0 for i in range(M+1)]
dp[0] = 1

for i in C :
    for j in range(i, M+1):
        if j - i >= 0 :
            dp[j] += dp[j-1]
            
print(dp[M])