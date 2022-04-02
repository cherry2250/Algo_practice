from collections import deque

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    que = deque([(n, 0)])
    v = set()
    v.add(n)

    while que:
        n, cnt = que.popleft()
        if n == m:
            break
        if n + 1 not in v and n + 1 <= 1000000:
            que.append((n + 1, cnt + 1))
            v.add(n + 1)
        if n - 1 not in v and n - 1 <= 1000000:
            que.append((n - 1, cnt + 1))
            v.add(n - 1)
        if n * 2 not in v and n * 2 <= 1000000:
            que.append((n * 2, cnt + 1))
            v.add(n * 2)
        if n - 10 not in v and n - 10 <= 1000000:
            que.append((n - 10, cnt + 1))
            v.add(n - 10)
    print(f'#{tc} {cnt}')