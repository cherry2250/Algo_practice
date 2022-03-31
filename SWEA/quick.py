def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    low, equal, high = [], [], []
    for num in arr:
        if num < pivot:
            low.append(num)
        elif num > pivot:
            high.append(num)
        else:
            equal.append(num)
    return quick_sort(low) + equal + quick_sort(high)
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = quick_sort(arr)
    print(f'#{tc} {ans[N//2]}')