import itertools
import sys 
input = sys.stdin.readline 

arr = list(int(input()) for _ in range(9))
arr.sort()
a = list(itertools.combinations(arr,7))
ans = []
for i in a:
    if sum(i) == 100 :
        for j in i :
            print(j, end='\n')
        break