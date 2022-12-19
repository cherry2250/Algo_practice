def solution(s):
    answer = []
    cnt = 0
    temp = 0

    while True : 
        if s == '1' :
            break

        temp = temp + s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]

        cnt = cnt + 1
    answer = [cnt, temp]
    return answer