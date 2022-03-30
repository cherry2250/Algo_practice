T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    time = []
    for i in range(N):
        A, B = map(int, input())
        arr.append([A,B])
        time.append(B-A)
        