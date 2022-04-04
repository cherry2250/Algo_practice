def comb(k,s):
    if k == R:
        print(*T)
    else :
        for i in range(s, N-R+k+1):
            T[k] = a[i]
            comb(k+1, i+1)
            
n = [[1,2,3],
     [4,5,6],
     [7,8,9]]
a = []
for i in range(len(n)):
    for j in range(len(n[i])):
        a.append(n[i][j])

N = len(a)
R = 3
T = [0]*R
comb(0,0)