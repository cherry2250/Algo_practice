import sys
# 떡의 개수, 떡의 길이
n, m = map(int, sys.stdin.readline().rstrip().split())
# 높이
n_list = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(n_list)

# 절단기의 높이
result = 0

while (start < end):
    mid = (start+end)//2
    sum = 0
    for n in n_list:
        # 떡의 높이가 더 높을 때
        if (n > mid):
            sum += n - mid
    if (sum < m):
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)