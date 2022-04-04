import itertools
import sys
input=sys.stdin.readline
 
l, c  = map(int, input().split())
arr = list(input().split())
arr.sort()
vow = ['a', 'e', 'i', 'o', 'u']
cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
ans = list(itertools.combinations(arr, l))

for i in ans :
    v = 0
    c = 0
    for j in i:
        if j in vow :
            v += 1
        elif j in cons:
            c += 1
    if v >= 1 and c >= 2:
        print(''.join(i))