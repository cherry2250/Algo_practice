arr = list(map(int, input().split()))
ans = list(map(int, input().split()))
res = 0
for i in range(len(arr)):
    if arr[i] < ans[i] :
        res += ans[i] - arr[i]
print(res)