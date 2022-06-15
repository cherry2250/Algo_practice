def solution(new_id):
    answer = ""
    
    #1단계 소문자 만들기
    new_id = new_id.lower()
    
    #2단계 소문자, 숫자, -, _, .만 사용
    for value in new_id :
        if value.islower() or value.isdigit() or value in ["-","_", "." ] :
            answer += value
    
    #3단계 . 두번 이상 반복되는 경우 .으로 변경
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    #4단계 .가 처음이나 끝에 위치하면 삭제
    if answer[0] == ".":
        if len(answer) >= 2:
            answer = answer[1:]
        else:
            answer = "."
    
    if answer[-1] == ".":
        answer = answer[:-1]
    
    #5단계 빈 문자열인 경우 a대입
    if answer == "":
        answer = "a"
    
    #6단계 16자리 이상인 경우 15자리까지 변경 / 마지막자리 .인지 확인
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    
    #7단계 2자 이하인 경우 마지막 문자 추가
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer