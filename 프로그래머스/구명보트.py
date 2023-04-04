#실패코드
#처음에는, 정렬해서 가벼운애들부터 쭉 태우려고 했었음
def solution(people, limit):
    people.sort()
    now = 0
    boat = 1
    for i in range(len(people)):
        if now + people[i] <= limit :
            now += people[i]
        else :
            now = people[i]
            boat += 1
    return boat

#그다음, while people을 걸어두고, pop을 하면서 하나씩 지우는 방식 -> 효율성 통과 못함

#성공코드
#투포인터를 사용하는 방식으로 pop이나 remove의 계산 과정 없이 진행
def solution(people, limit):
    people.sort()
    boat = 0
    start, end = 0, len(people)-1
    while start <= end:
        boat += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
    return boat