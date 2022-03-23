#좋은 단어

T = int(input())
cnt = 0
for tc in range(1, T+1):
    arr = list(input())
    N = len(arr)
    ans = []
    for i in range(N):
        if ans and arr[i] == ans[-1]:
            ans.pop()
        else:
            ans.append(arr[i])
    if not ans:
        cnt += 1
print(cnt)