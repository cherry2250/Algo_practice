import sys

arr = list(map(int, input().split()))
if arr[0] > arr[1] :
    print('A')
elif arr[1] > arr[0] :
    print('B')
else :
    print('same')