import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    total = 0
    for item in arr :
        if item % 2 == 1 :
            total += item
            
    print(f'#{test_case} {total}')
    
