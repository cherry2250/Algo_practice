def solution(s):
    ans = len(s) 
    
    # 최소 길이 계산
    for a in range(1, len(s)//2+1): #절반까지만 가면 되니까
        result = "" 
        slice = s[0:a] #s배열 a만큼 자름 (비교)
        
        cnt = 1 
        for i in range(a, len(s), a): #a부터 끝까지 a크기씩 이동
            # 반복이 있을 때
            if slice == s[i: i+a]: #이전상태랑 동일하면
                cnt += 1 #카운트 추가
            # 반복이 추가로 없을 때
            else:
                if cnt == 1: 
                    result += slice #카운트 숫자 안넣어도 됨
                    slice = s[i: i+a] #상태 초기화
                else: 
                    result += (str(cnt) + slice)
                    cnt = 1 #카운트 초기화
                    slice = s[i: i+a] #상태 초기화
        
        # 남아있는 문자열
        if cnt == 1: 
            result += slice
        else: result += (str(cnt) + slice)
            
        ans = min(ans, len(result)) #min값 구함
    
    return ans