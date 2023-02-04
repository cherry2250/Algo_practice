num = list(input())
arr = []
for i in num:
    arr.append(int(i))
arr.sort(reverse=True)
ans = ''
if sum(arr) % 3 != 0:
    print(-1)
elif 0 not in arr:
    print(-1)
else :
    for i in range(len(arr)):
        ans += (str(arr[i]))
    print(ans)