import sys
input = sys.stdin.readline

T = int(input())
arr = [list(input().rstrip()) for _ in range(T)]

alphabet = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

#자리수 기록
for i in arr:
    for j in range(len(i)):
        num = 10 ** (len(i)-j-1)
        alphabet[i[j]] += num 

# alphabet.sort() #딕셔너리 정렬 어떻게 하나요..?
s = sorted(alphabet.values(), reverse=True)
result = 0
max = 9
for num in s:
    if num : 
        result += num * max
        max -= 1
print(result)