def solution(n, lost, reserve):
    answer = 0
    student = [0]*(n+2)
    for i in reserve:
        student[i] += 1
    for j in lost:
        student[j] -= 1

    for i in range(1, n+1):
        if student[i] > 0:
            if student[i-1] < 0:
                student[i] -= 1
                student[i-1] += 1
            elif student[i+1] < 0:
                student[i] -= 1
                student[i+1] += 1

    for i in range(1, n+1):
        if student[i] > -1:
            answer += 1

    return answer