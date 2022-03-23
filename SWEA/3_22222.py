T = int(input())
for i in range(1, T+1):
    t = int(input())
    nums = sorted(list(map(int, input().split())))
    arr = []

#접근 방법 :
#1. 값을 리스트로 정렬함
#2. 리스트를 반으로 나눠서 2개의 리스트로 분류 ex. 1~10까지면 1~5까지의 리스트 1개, 6~10까지 1개
#3. 큰 값이 든 리스트를 reverse함 ex. 1~5까지 리스트, 10~6까지 리스트
#4. 두 개의 리스트를 빈 리스트에 교차로 넣음