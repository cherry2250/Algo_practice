import sys

sys.stdin = open("input.txt", "r")
T = (input())

center = len(T) // 2
sorted_nums = sorted(T)
print(sorted_nums[center])