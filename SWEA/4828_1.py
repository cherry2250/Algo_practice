T = int(input())

for i in range(1, T + 1):
    n = int(input())
    a = list(map(int, input().split()))
    print(f'#{i} {max(a) - min(a)}')