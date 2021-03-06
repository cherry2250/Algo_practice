def solution(n, works): #n = 시간 / works = 작업량
    while n > 0:
        M = max(works)
        if sum(works) == 0:
            break
        works[works.index(M)] -= 1
        n -= 1
        arr = []
        for x in works :
            arr.append(x**2)
    return sum(arr)


def solution(n, works): #n = 시간 / works = 작업량
    if n >= sum(works):
        return 0
    while n > 0 :
        works.sort()
        works[-1] -= 1
        n -= 1
        arr = []
        for x in works :
            arr.append(x**2)
    return sum(arr)

#시간 때문에 1씩 감소시키는 것이 아니라
#가장 큰 수와 그 앞의 숫자의 차이를 한 번에 줄이니까 시간 단축됨

def soultion(n, works) :
    answer = 0
    works.append(0) #최소값 확인을 위해
    works.sort()
    for i in range(1, len(works)): #인덱싱 편하도록 i는 1부터 시작
        tmp = works[-i] - works[-(i + 1)] #가장 높은 수와 그다음 높은 수의 차이 기록
        if tmp * i < n : #그 차이 X 몇 번째인지가 n보다 작으면
            n -= tmp * i #그만큼 n을 빼줌
            for j in range(1, i+1): 
                works[-j] -= tmp #첫번째 큰 숫자와 다음을 같게 만든다
        else : #n보다 크면
            q = n // i #n에 대해서 몇 번째인지로 나눈다. #몫
            n = n % i #나머지
            for j in range(1, i+1) :
                works[-j] -= q #제일 뒤 숫자부터 i번째까지 몫만큼 빼줌
            for j in range(1, n+1) :
                works[-j] -= 1 #나머지 처리
            break
    for i in works : 
        answer += i ** 2
    return answer