#저의 최애 내장함수.. permutation으로 풀었습니다

from itertools import permutations

def solution(k, dungeons): #k = 현재 피로도, dungeons = 피로도 리스트
    answer = -1
    arr = list(permutations(dungeons, len(dungeons))) #순열 만들기
    
    for i in arr: #순열 탐색(전장 탐험)
        las = k #갱신할 피로도 변수
        count = 0 #탐험 회수 카운트
        for j in i:
            if las >= j[0]: #남은 피로도가 최소 피로도 보다 크면 탐험 가능
                #이 때 j[0]은 j[1]보다 항상 크다고 문제에서 제시해줬기 때문에 추가적인 if 생략 가능
                las -= j[1] #탐험하면서 소모된 피로도 빼줌
                count += 1 #전장 탐험 완료
        if count > answer: #max값 갱신
            answer = count
    
    return answer