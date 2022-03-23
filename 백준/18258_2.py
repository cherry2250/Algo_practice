import sys 
input = sys.stdin.readline 

T = int(input()) 
que = []
index = 0 

for tc in range(T): 
    arr = list(input().split())
    if arr[0] == 'push': 
        que.append(int(arr[1]))
        
    elif arr[0]=='pop': 
        if len(que)-index == 0: 
            print(-1) 
        else: 
            print(que[index]) 
            index += 1 #pop을 안하고 삭제했어야 하는 위치를 기억
            
    elif arr[0]=='size': 
        print(len(que)-index) 
    
    elif arr[0] =='empty': 
        if len(que)-index == 0: 
            print(1) 
        else: 
            print(0) 
    
    elif arr[0] == 'front': 
        if len(que)-index == 0: 
            print(-1) 
        else: 
            print(que[index])
            
    elif arr[0] == 'back': 
        if len(que)-index == 0: 
            print(-1)
        else: 
            print(que[-1])
