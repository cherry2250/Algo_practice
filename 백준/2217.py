N = int(input())
arr = sorted([int(input()) for _ in range(N)], reverse=True)
for i in range(len(arr)):
    arr[i] = arr[i] * (i+1)
print(max(arr))