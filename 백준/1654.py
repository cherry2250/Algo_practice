#이분탐색 문제  / 기준 : 랜선의 개수
#찾아야 하는 값 = 랜선의 길이
from sys import stdin
input = stdin.readline 

k, n = map(int, input().split()) 

arr = []
for _ in range(k) :
    arr.append(int(input()))
    
low = 1 #최소값
high = max(arr) #최대값
res = 0

while low <= high :
    mid = (low + high) // 2 #중간값, 몇 cm 크기로 자를 것인지
    cut = [] #모인 랜선을 합쳐줄 빈 배열
    for i in arr :
        cut.append(i // mid) #cut배열에 잘라낸 랜선 모음
        
    if sum(cut) >= n : #잘라낸 개수가 기준보다 많다면
        res = mid
        low = mid + 1 #더 큰 단위로 잘라서 개수 줄임
    elif sum(cut) < n: #잘라낸 개수가 기준보다 적으면
        high = mid -1 #더 작은 단위로 잘라서 개수 늘림
print(res)