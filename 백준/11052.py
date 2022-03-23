import sys
input = sys.stdin.readline

# T = int(input())
# arr = list(map(int, input().split()))
# list_a = []
# if T % 2 == 0:
#     for i in range(len(arr)//2):
#         S = arr[i] + arr[-i-1]
#         list_a.append(S)
# else :
#     for i in range(len(arr)//2):
#         S = arr[i] + arr[-i-2]
#         list_a.append(S)
#     list_a.append(arr[-1])
# print(max(list_a))

T = int(input()) 
arr = [0] + list(map(int, input().split())) 
dp = [0]*(T+1) 

for i in range(1, T+1): 
    for j in range(1, i+1): 
        dp[i] = max(dp[i], dp[i-j]+arr[j]) 

print(dp[T])

# D[i] 를 카드 i개를 사는 최대 금액이라고 정의한다고 하자.
# 카드 i개를 사는 방법은 
# 1. 카드가 1개 포함된 카드팩 + 카드 (i-1)장 구매
# 2. 카드가 2개 포함된 카드팩 + 카드 (i-2)장 구매 
# 3. 카드가 3개 포함된 카드팩 + 카드 (i-3)장 구매 ...로 이어진다.
# -> 일반화하면 카드가 j개 포함된 카드팩 + 카드 (i-j)장 구매
