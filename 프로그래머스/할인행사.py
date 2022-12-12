def solution(want, number, discount):
    answer = 0
    dic = {want[i] : number[i] for i in range(len(want))}
    for i in range(len(discount) - sum(number) + 1):
        temp = dict()
        for j in range(i, i + sum(number)):
            if discount[j] in temp.keys() :
                temp[discount[j]] += 1
            else:
                temp[discount[j]] = 1
        if temp == dic:
            answer += 1
    return answer