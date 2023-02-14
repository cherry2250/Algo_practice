import itertools
import sys 
input = sys.stdin.readline 

arr = list(int(input()) for _ in range(9))
arr.sort()
a = list(itertools.combinations(arr,7))
ans = []
for i in a:
    if sum(i) == 100 :
        for j in i :
            print(j, end='\n')
        break


height = [0, 0, 0, 0, 0, 0, 0, 0, 0]
flag = 0
for i in range(9):
    h = int(input())
    height[i] = h

height.sort()
sum = sum(height)
for i in range(8, -1, -1):
    for j in range(7, -1, -1):  #2가지의 수를 뺴는 모든 경우의 수를 따져 봄.
        sum -= height[i]+height[j]  #일단 뺴보고
        if(sum != 100): #아니다 싶으면
            sum += height[i]+height[j]  #다시 더해주고
        else:   #이게 맞는가 싶으면
            height[i] = height[j] = 0   #뺐었던 수의 자리를 0으로 대체
            flag = 1    #while 탈출용 flag
            break
    if flag:
        break

for res in height:  
    if res: #뺐었던 수를 제외하고 출력
        print(res)