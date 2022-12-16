def solution(s):
    answer = 0
    temp = list(s)
    for i in range(len(s)):
        arr = []
        for j in range(len(temp)):
            if len(arr) > 0 :
                if arr[-1] == '[' and temp[j] == ']':
                    arr.pop()
                elif arr[-1] == '(' and temp[j] == ')':
                    arr.pop()
                elif arr[-1] == '{' and temp[j] == '}':
                    arr.pop()
                else : 
                    arr.append(temp[j])
            else:
                arr.append(temp[j])
        if len(arr) == 0 :
            answer += 1
        temp.append(temp.pop(0))
    return answer