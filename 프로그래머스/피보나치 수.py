def solution(n):
    answer = [0, 1]
    for i in range(n-1) :
        answer.append(answer[i] + answer[i+1])
    return answer[n] % 1234567