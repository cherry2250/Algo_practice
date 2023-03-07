import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(1, N+1):
    name, korean, english, math = map(str, input().split())
    korean = int(korean)
    english = int(english)
    math = int(math)
    arr.append([korean, english, math, name])

arr.sort(key=lambda x:(-x[0], x[1], -x[2], x[3]))
for i in range(len(arr)):
    print(arr[i][3])