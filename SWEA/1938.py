#간단한 계산기
import math
arr = list(map(str, input().split()))
print(int(arr[0]) + int(arr[1]))
print(int(arr[0]) - int(arr[1]))
print(int(arr[0]) * int(arr[1]))
print(math.trunc(int(arr[0]) / int(arr[1])))