import itertools

while True:
    arr = list(map(int, input().split()))
    ans = []
    if arr[0] == 0:
        break
    arr.pop(0)
    result = list(itertools.combinations(arr, 6))
    for i in result : 
        for j in i:
            print(j, end=' ')
        print()
    print()