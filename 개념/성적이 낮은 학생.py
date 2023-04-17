n = int(input())
arr = [list(input().split()) for _ in range(n)]
arr = sorted(arr, key=lambda x:x[1])
print(arr)
for i in arr:
	print(i[0], end=' ')