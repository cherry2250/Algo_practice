T = int(input())
for tc in range(1, T+1):
    word = list(map(str, input()))
    for i in range(len(word)):
        if i == word[::-1]:
            print(1)
        else : 
            print(0)