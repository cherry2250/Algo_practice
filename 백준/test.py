import sys
input = sys.stdin.readline

N = int(input())
arr = []
res = []
check = [0] * 1,000,000,000
cnt = 0
for i in range(N):
    n = int(input())
    arr.append(n)
    check[n] += 1
for j in range(N):
    res.append(arr[j] - arr[j-1])
for x in range(N):
    if check[arr[x] + min(res)] == 0 :
        check[arr[x] + min(res)] = 'O'
        cnt += 1
print(cnt)
        