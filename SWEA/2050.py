#알파벳을 숫자로

T = input()
arr = list(T)
arr_1 = []
for i in arr:
    a = ord(i) - 64
    arr_1.append(a)
print(' '.join(str(j)for j in arr_1))