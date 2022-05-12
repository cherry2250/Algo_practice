#ban 당할 수 있는 조합 (중복 없어야 하기 때문에) 만들고
#banned_id 원소랑 길이 비교 -> 값 비교

from itertools import combinations

def solution(user_id, banned_id):
    arr = combinations(user_id, len(banned_id)) #ban 당할 수 있는 모든 조합 만들기
    for i in arr:
        if len(i[0]) != len(banned_id[0]):
            return False
    answer = 0
    return answer