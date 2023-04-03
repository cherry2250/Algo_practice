n,m = map(int,input().split(' '))
s = list() #세트가격
o = list() #낱개 가격

for _ in range(m):
    a,b = input().split(' ')
    s.append(int(a)) #세트끼리
    o.append(int(b)) #낱개끼리

s = min(s)
o = min(o)

if s < o * 6:
    if s < (n % 6) * o:
        print((n // 6) * s + s)
    else:
        print((n // 6) * s + (n % 6) * o)

elif s >= o * 6:
    print(n * o)