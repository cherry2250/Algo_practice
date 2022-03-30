def merge_sort(arr):
  # 전체를 절반으로 나누고
  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]
  # 나뉜 각각을 정렬하고
  left = merge_sort(left)
  right = merge_sort(right)
  # 정렬된 각각을 병합
  return merge(left, right)
  
  
def merge(left, right):
  result = []
  i = j = 0
  while :
    if left[i] < right [j]:
      result.append(left[i])
      i += 1
    else :
      result.append(right[j])
      j += 1
     
  return result