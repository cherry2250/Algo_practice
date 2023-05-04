def solution(msg):
    answer = []

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = dict(zip(alphabet, range(1, 27)))
    print(dic)

    w, c = 0, 0
    while True:
        c += 1	
        if c == len(msg):	
            answer.append((dic[msg[w:c]]))
            break
        
        # 만약 [현재글자+다음글자]가 사전에 없다면
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1 # 사전에 추가
            answer.append(dic[msg[w:c]])
            w = c	# 현재글자를 다음글자로 옮겨줌
            
        # 만약 [현재글자+다음글자]가 사전에 있다면 w의 값은 변하지 않고 c의 값만 1씩 증가한다. 
    return answer