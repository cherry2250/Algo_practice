def solution(order):
    truck = []
    idx = 1
    now = 0
    while idx < len(order) + 1:
        truck.append(idx)
        while truck[-1] == order[now]:
            now += 1
            truck.pop()
            if len(truck) == 0 :
                break
        idx += 1
    
    return now