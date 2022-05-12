#permutation으로 풀어봤는데 시간 초과함..
from itertools import permutations

def solution(numbers):
    answer = ''
    arr = permutations(numbers)
    m_num = 0
    for i in arr:
        res = int(''.join(map(str, i)))
        if m_num < res:
            m_num = res
    answer = str(m_num)
    return answer

#틀림.. 
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers)) #문자열로 변환한다음에 정렬
    numbers.sort(reverse=True)
    for i in numbers :
        answer += (i)
    return answer

    