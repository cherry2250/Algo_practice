#오큰수
from sys import stdin
input = stdin.readline

N = int(input()) #숫자 입력
arr = list(map(int, input().split())) #리스트 입력
stack =[] #인덱스 번호 입력 받을 것
ans = [-1] * N #인덱스 번호에 해당하는 값 입력
for i in range(len(arr)): 
    while stack and arr[stack[-1]] < arr[i]: #맥스값을 찾는 것과 같이
        ans[stack[-1]] = arr[i] #-1이 담겨있는 곳에 맥스 인덱스값의 해당값으로 바꿔줌 
        stack.pop() #없앰
    stack.append(i) #인덱스 값 추가
print(*ans)