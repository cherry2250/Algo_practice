def binarySearch(start, end, key, count) : 
    start = 0
    count = 0
    while start <= end : 
        count += 1
        middle = start + (end - start) // 2 # end //2 랑 같음
        if key == middle : #검색성공
            return count
        elif key > middle : #오른쪽에 있을 때
             end = middle -1
        else :
            start = middle + 1
    return False # 검색실패

T = int(input())
for i in range(1,T+1) : 
    P, A, B = map(int, input().split())
    Person_A = binarySearch(0, P, A, 0)
    Person_B = binarySearch(0, P, B, 0)
    if Person_A > Person_B:
        print(f'#{i+1} B')
    elif Person_A < Person_B:
        print(f'#{i+1} A')
    else:
        print(f'#{i+1} 0')