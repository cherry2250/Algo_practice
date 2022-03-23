T = int(input())
for tc in range(1, T+1):
    S = list(input())
    arr = []
    for i in range(len(S)):
        if arr and S[i] == arr[-1]:
            arr.pop()
        else:
            arr.append(S[i])
    print(f'#{tc} {len(arr)}')