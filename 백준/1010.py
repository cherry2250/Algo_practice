import math
t = int(input())
for tc in range(t):
    N, M = map(int, input().split())

    X = math.factorial(M)
    Y = (math.factorial(M-N)) * (math.factorial(N))

    answer = X//Y

    print(answer)