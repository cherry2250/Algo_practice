def solution(citations):
    citations.sort(reverse=True) #정렬
    n = len(citations) #길이
    ans = 0 #정답 변수
    for h in range(n): #길이만큼 돌면서
        # if citations[h] >= n-h: 정렬을 뒤집지 않았을 경우
        if citations[h] <= h: #h번 이상 인용된 논문이 h편 이상
            ans = h #정답 출력
            break
    return n #if 조건에 해당하지 않는 경우


def solution(citations):
    citations.sort(reverse=True) #정렬
    n = len(citations) #길이
    ans = n #정답 변수
    for h in range(n): #길이만큼 돌면서
        if citations[h] <= h: #h번 이상 인용된 논문이 h편 이상
            ans = h #정답 출력
            break
    return ans #if 조건에 해당하지 않는 경우