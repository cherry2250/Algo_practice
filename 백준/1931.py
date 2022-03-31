import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(N)])
cnt = 1
now = arr[0]
for i in range(1, N):
    if now[0] < arr[i][0]: #시작시간이 현재 이후고
        if now[1] <= arr[i][0]: #끝났는데, 시작 시간보다 여유 있다면
            now = arr[i] #now 갈아치움
            cnt += 1 
        elif now[1] > arr[i][1]: #끝나는 시간이 느리면
            now = arr[i] # now 갈아치움 / 카운트 금지
    elif now[0] == now[1]: #시작시간과 끝나는 시간이 똑같을 땐
        now = arr[i] #다음 회의 시작
        cnt += 1 
print(cnt)