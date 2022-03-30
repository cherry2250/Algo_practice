def merge_sort(arr):
    if len(arr) == 1:
        return arr
    #전체를 절반으로 나누고
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    #나뉜 각각을 정렬하고
    left = merge_sort(left)
    right = merge_sort(right)
    #정렬된 각각을 병합
    return merge(left, right)

def merge (left, right):
    global cnt
    result = []
    i = j = 0
    left_length = len(left)
    right_length = len(right)
    if left[-1] > right[-1]:
        cnt += 1
    while i < left_length or j < right_length :
        #left와 right 둘 다 요소가 남아있ㄷ으면
        if i < left_length and j < right_length:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else :
                result.append(right[j])
                j += 1
        else : #둘 중 하나는 이미 비교할 요소가 없음
            if  i < left_length : #왼쪽 요소가 남음
                result.append(left[i])
                i += 1
            else : #오른쪽 요소가 남음
                result.append(right[j])
                j += 1
                
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(arr)
    print(f'#{tc} {result[N//2]} {cnt}')