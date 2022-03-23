import sys

sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    a = sum(arr) / len(arr)
    b = int(round(a,0))
            
    print(f'# {b}')



T = int(input())
  
list_a = []
for i in range(T):
    arr = list(map(int,input().split()))
    list_a.append(arr)
  
def get_avg(list_a):
    avg_list = [] #각 리스트 평균들 저장할 리스트
    for lst in list_a:
        total = 0 #리스트 하나 돌 때마다 리스트 합 초기화
        for i in lst:
            total = total + i
            avg = total / len(lst)
        avg_list.append(avg) #각 리스트 평균들 리스트에 리스트 평균 추가 
    return enumerate(avg_list,start=1) #인덱스를 1부터 시작하여 리스트 원소 불러옴
  
for i in range(T):
    print(f'#{list(get_avg(list_a))[i][0]} {round(list(get_avg(list_a))[i][1])}')
    
    