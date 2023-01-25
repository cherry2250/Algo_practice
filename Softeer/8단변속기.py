import sys

arr = list(map(int, input().split()))
yes = 0
if yes == 0 :
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1] + 1:
            continue
        else :
            yes = 1
            break
if yes == 1 :
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1] -1 :
            continue
        else :
            yes = 2
            break

if yes == 0:
    print('ascending')
elif yes == 1:
    print('descending')
else : 
    print('mixed')