def solution(name, yearning, photo):
    answer = []
    dict = {}
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    print(dict)
    for i in range(len(photo)):
        cnt = 0
        for j in photo[i]:
            if j in name:
                cnt += dict[j]
        answer.append(cnt)
    return answer