#완전 탐색 -> 효율성
#리스트 투포인터 -> 효율성

#딕셔너리 투포인터 써야 한다네요..

def solution(gems):
    left, right = 0, 0
    targets = set(gems)
    N = len(gems)
    answer = [1, N]
    tmp = []
    while True:
        if gems[right] not in tmp:
            tmp.append(gems[right])
        right += 1
        if len(tmp) == len(targets):
            while gems[left] in gems[left+1:right]:
                left += 1
            if answer[1] - answer[0] > right - left-1:
                answer = [left+1, right]
            if right - left +1 == len(targets):
                return answer
        if (right == N):
            return answer