import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    p = input().rstrip().replace("RR", "")
    n = int(input())
    arr = []
    if n == 0:
        input() 
    else:
        arr = [*map(int, input().rstrip()[1:-1].split(","))] 
    q = deque(arr)
    is_occured_error = False
    is_reversed = False
    
    for cmd in p:
        if cmd == "R":
            is_reversed = False if is_reversed else True
        elif cmd == "D":
            if q:
                if is_reversed:
                    q.pop()
                else:
                    q.popleft()
            else:
                is_occured_error = True
                break
    
    if is_occured_error:
        print("error")
    else:
        if is_reversed:
            q.reverse()
        
        print("[" + ",".join(map(str, q)) + "]")