import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(lambda x: int(x) if x.isdigit() else x, input().split())) for _ in range(n)]
for l in sorted(lst, key=lambda x: (-x[1], x[2], -x[3], x[0])):
    print(l[0])
