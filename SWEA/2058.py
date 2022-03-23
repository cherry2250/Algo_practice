#자연수 덧셈

T = int(input())

arr = list(map(int, str(T)))
total = 0
for i in arr:
    total +=i

print(total)