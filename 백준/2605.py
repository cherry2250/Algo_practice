T = int(input())
arr = list(map(int, input().split()))
ans = arr.set()
print(len(arr) - len(ans))