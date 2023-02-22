import sys
from collections import Counter
input = sys.stdin.readline

def get_most_freq_value(nums):
    cnt = Counter(nums)
    try:
        check = cnt.most_common(2)
        if check[0][1] < check[1][1]: # 개수가 적다면
            return check[0][0]
        
        elif check[0][1] == check[1][1]: # 개수가 같다면
            return check[1][0]

    except IndexError:
        check = cnt.most_common(1)
        return check[0][0]

def get_value_range(nums):
    if len(nums) == 1:
        return 0
    else:
        return (nums[-1] - nums[0])

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()
print (round(sum(nums)/len(nums))) # 산술평균
print (nums[int(len(nums)/2)]) # 중앙값
print (get_most_freq_value(nums)) # 최빈값
print (get_value_range(nums)) # 범위