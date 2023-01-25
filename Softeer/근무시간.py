import sys
ans = 0
for i in range(5):
    A, B = input().split()
    A1, A2 = A.split(':')
    a1, a2 = int(A1), int(A2)
    B1, B2 = B.split(':')
    b1, b2 = int(B1), int(B2)
    minit = b2 - a2
    hour = 60 * (b1 - a1)
    ans += minit + hour

print(ans)