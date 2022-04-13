N, M = map(int, input().split())
a = set()
for _ in range(N):
    s = input()
    a.add(s)
b = set()
for _ in range(M):
    b.add(input())
res = sorted(list(a&b))

print(len(res))
for k in res:
    print(k)