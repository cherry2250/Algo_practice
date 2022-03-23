import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    arr_b = ' '.join(arr[::-1])
    print(f'Case #{tc}: {arr_b}')