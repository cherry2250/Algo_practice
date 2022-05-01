#실패 => 효율성 통과 못함
def solution(participant, completion):
    participant.sort() #정렬
    completion.sort() #정렬
    while len(completion) != 0:
        for i in participant:
            if i in completion: #같은 값을 찾으면 동시에 삭제
                a = completion.index(i) #.index도, pop도 시간 소요가 큰데 2개 배열 모두 하면 2배로 걸림
                completion.pop(a)
                b = participant.index(i)
                participant.pop(b)
    return participant[0]

#성공 
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]: #위치가 같은데 값이 다른 것만 찾으면 된다
            return participant[i]
    return participant[-1]