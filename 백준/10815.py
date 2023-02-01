import sys

def binary_search (array, target, start, end):
    while start <= end :
        mid = (start + end) //2 
        if array[mid] == target :
            return mid
        
        elif array[mid] > target :
            end = mid - 1
        
        else :
            start = mid + 1
    return None

N = int(input())
arr = sorted(list(map(int, sys.stdin.readline().split())))
M = int(input())
card = list(map(int, sys.stdin.readline().split()))
ans = []

for i in card :
    result = binary_search(arr, i, 0, len(arr)-1)
    if result == None:
        ans.append(0)
    else :
        ans.append(1)

print(*ans, sep=' ')
