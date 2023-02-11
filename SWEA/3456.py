from collections import defaultdict
for tc in range(int(input())):
    nums = list(map(int, input().split()))
    d = defaultdict(int)
    for num in nums:
        d[num] +=1
    for k,v in d.items():
        if v==1 or v==3:
            result = k
            break
    print("#{} {}".format(tc+1,result))