arr = list(input())
exam = list(input())
arr_2 = []
num = []
for i in range(len(arr)):
    try:
        num.append(int(arr[i]))
    except ValueError:
        arr_2.append(arr[i])
ans = []
for i in range(len(exam)) :
    if exam[i] in arr_2 :
        ans.append(arr_2.index(exam[i]))
ans.sort()
res = 0
if len(exam) == len(ans):
    for i in range(len(ans)-1):
        if ans[i] == ans[i+1] -1:
            res = 1
        else : 
            res = 0
print(res)
