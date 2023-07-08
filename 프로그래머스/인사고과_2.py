def solution(scores):
    n = len(scores)
    wh_score = scores[0][0]  # 완호의 근무 태도 점수
    wh_eval = scores[0][1]   # 완호의 동료 평가 점수

    # 완호의 점수가 다른 사원들의 점수보다 모두 높은지 확인
    if all(wh_score >= s[0] and wh_eval >= s[1] for s in scores[1:]):
        return -1

    # 완호를 제외한 다른 사원들의 점수 합을 구함
    total_scores = sum(s[0] + s[1] for s in scores[1:])

    # 완호의 점수를 추가하여 전체 점수 합과 인원 수를 구함
    total_scores += wh_score + wh_eval
    num_people = n

    # 점수 합과 인원 수를 바탕으로 완호의 석차를 구함
    rank = 1
    for s in scores[1:]:
        score_sum = s[0] + s[1]
        if score_sum > total_scores / num_people:
            rank += 1

    return rank