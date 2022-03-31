n = int(input())
arr = [500, 100, 50, 10, 5, 1]
K = 1000 - n
cnt = 0
for i in arr:
    if K // i != 0:
        cnt += (K//i)
        K = K % i
print(cnt)