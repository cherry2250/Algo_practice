def solution(ingredient):
    answer = 0
    arr = []
    for i in ingredient : 
        arr.append(i)
        if arr[-4:] == [1, 2, 3, 1]:
            answer += 1
            for j in range(4):
                arr.pop()
    return answer