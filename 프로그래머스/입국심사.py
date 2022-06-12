import heapq
def solution(n, times):
    fin = 0
    info= [ [i,i] for i in times]
    answer=0
    while fin<n:
        end,dur=heapq.heappop(info)
        answer=max(answer,end)
        fin+=1
        heapq.heappush(info,[end+dur,dur])
    return answer