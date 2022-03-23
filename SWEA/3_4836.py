T = int(input()) 

for i in range(1, T+1):
    t = int(input())
    arr = [[0]*11 for j in range(10)] # 10X10 배열 생성
    for j in range(t)):
        x1, y1, x2, y2, color = map(int, input().split())
#접근 방법 :
#1. 조건으로 빨간색, 파란색을 구분하여
#2. 빨간색일 때, 값이 있는지 확인 -> 있으면 보라색, 없으면 빨간색
#3. 파란색일 때, 값이 있는지 확인 -> 있으면 보라색, 없으면 파란색
#4. 보라색 값 개수 확인 -> 이거 어떻게 할까요..?