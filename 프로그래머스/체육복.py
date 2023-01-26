n = 5
lost = [2, 4]
reserve = [1, 3, 5]
answer = 0
arr = [0] * (n + 1)

for i in reserve :
    arr[i] = 1

for j in lost :
    if j-1 in reserve :
        arr[j] = 1
        a = reserve.index(j-1)
        print(a)