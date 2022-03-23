N = int(input())
list_a = list(range(1,N+1))
arr = list(map(str, list_a))
list_b = []
for i in arr:
    if i in '3' or i in '6' or i in '9':
        list_b.append('-')
    else : 
        list_b.append(i)

print(' '.join(list_b))

N = int(input())
for i in range(1, n+1):
    s = str(i)
    cnt = 0
    for j in s:
        if (j =='3') or (j =='6') or (j =='9'):
            cnt += 1 #36처럼 2번 나올 수 있으니까
        if cnt == 0:
            print(i, end=' ')
        else :
            print(cnt*'-', end=' ')