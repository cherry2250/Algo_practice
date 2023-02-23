N = int(input())
strN_list = []

for i in str(N):
    strN_list.append(i)

strN_list.sort(reverse=True)

ans = ''
for i in strN_list:
    ans+=i
print(int(ans))