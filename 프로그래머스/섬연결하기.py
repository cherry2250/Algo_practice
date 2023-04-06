def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2]) 
    line = set([costs[0][0]]) 
    while len(line) != n:
        for cost in costs:
            if cost[0] in line and cost[1] in line:
                continue
            if cost[0] in line or cost[1] in line: 
                line.update([cost[0], cost[1]])
                answer += cost[2]
                break
                
    return answer