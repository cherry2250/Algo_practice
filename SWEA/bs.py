def binary_search(arr, target): 
    global tem 
    left = 0 
    right = N - 1 
    
    while left <= right: 
        mid = (left + right) // 2 
        
        if arr[mid] == target: 
            return mid
        
        elif arr[mid] > target: 
            if tem == 'left': 
                return -1 
            right = mid - 1 
            tem = 'left' 
        
        else: 
            if tem == 'right': 
                return -1 
            
            left = mid + 1 
            tem = 'right' 
    
    return -1 

T = int(input()) 
for tc in range(1, T+1): 
    N, M = map(int, input().split()) 
    A = list(map(int, input().split())) 
    B = list(map(int, input().split())) 
    A.sort() 
    cnt = 0 
    for target in B: 
        tem = '' 
        idx = binary_search(A, target) 
        if idx != -1: 
            cnt += 1 
    print(f'#{tc} {cnt}')
