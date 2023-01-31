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

#정답 코드
def solution(numbers):
    arr = []
    for i in numbers:
        a = str(i)
        arr.append(a)
    arr.sort(key=lambda x: x * 3, reverse=True)
    ans = ''
    for i in range(len(arr)):
        ans += arr[i]
    if int(ans) == 0:
        ans = '0'
    return ans # return str(int(''.join(arr)))