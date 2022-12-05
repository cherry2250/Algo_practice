from itertools import permutations
from collections import deque

def solution(expression):
    answer = 0
    ex = ["*", "-", "+"]

    li = []
    s = 0
    for i, v in enumerate(expression):
        if v in ["*", "-", "+"] :
            li.append(expression[s:i])
            li.append(v)
            s = i + 1
    else : 
        li.append(expression[s:])

    for e in ex:
        if e not in expression:
            ex.remove(e)

    primarity = permutations(ex)

    for j in primarity:
        stacks = [deque(li), deque()]
        t = 1
        for z in j:
            t = (t + 1) % 2
            t2 = (t + 1) % 2
            while len(stacks[t]):
                item = stacks[t].popleft()
                if len(stacks[t2]) and stacks[t2][-1] == z :
                    z = stacks[t2].pop()
                    n = stacks[t2].pop()
                    item = str(eval(str(n) + z + str(item)))
                stacks[t2].append(item)

        result = stacks[len(ex)%2].pop()
        result = abs(int(result))
        answer = max(answer, result)

    return answer