import sys
input = sys.stdin.readline

n, m = map(int, input().split())
video = list(map(int, input().split()))

#left는 동영상 길이의 최솟값 right는 동영상 길이의 최댓값
start = max(video)
end = sum(video)

res = 10**9
while(start <= end):
    mid = (start+end)//2
    cnt = 1
    tmp = 0
    for i in range(n):
        if(tmp+video[i] <= mid):
            # 만약 현재 블루레이에 비디오를 더 넣을 수 있다면
            tmp += video[i]
        else:
            cnt += 1
            tmp = video[i]
        if(cnt > m):
            break
    if(cnt > m):
        start = mid+1
    else:
        end = mid-1
        if(mid >= start):
            res = min(res, mid)

print(res)