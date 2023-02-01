def binary_search (array, target, start, end):
    flag = 0
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target :
            return 1
        elif array[mid] > target :
            if flag == 2:
                break
            else : 
                end = mid -1
                flag = 2
        else :
            if flag == 1:
                break
            else :
                start = mid + 1
                flag = 1
    return None

T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())
    array = sorted(list(map(int, input().split())))
    search = list(map(int, input().split()))
    cnt = 0
    for i in search:
        
        result = binary_search(array, i, 0, N-1)
        if result != None:
            cnt += 1
    print(f'#{tc} {cnt}')