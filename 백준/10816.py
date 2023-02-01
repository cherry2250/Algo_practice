import sys
input = sys.stdin.readline

def binary_serch(array, target, start, end):
    while start <= end :
        mid = (start + end) //2 
        if array[mid] == target : 
            s, e = 1, 1
            while mid - s >= start:
                if array[mid-s] != target:
                    break
                else :
                    s += 1
            while mid + e <= end:
                if array[mid + e] != target:
                    break
                else :
                    e += 1
            return s + e - 1
        elif array[mid] > target :
            end = mid - 1
        else :
            start = mid + 1
    
    return None

N = int(input())
card = sorted(list(map(int, input().split())))
M = int(input())
tar = list(map(int, input().split()))
ans = []
for i in tar :
    result = binary_serch(card, i, 0, N-1)
    if result == None:
        ans.append(0)
    else :
        ans.append(result)
print(*ans, end=' ')
