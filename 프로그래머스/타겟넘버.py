def solution(numbers, target):
    node = [] #노드의 합을 넣어줄 배열 생성
    node.append(0) #초기값 0을 넣어줌
    for i in numbers: #전체 입력을 돌면서
        arr = [] # 합계를 담아줄 임시 배열 생성
        for j in node: #노드값만큼 돌면서 (2의 배수만큼 증가할 것임)
            arr.append(i+j) #더한 값 넣어주고
            arr.append(j-i) #뺀 값 넣어줌
        node=arr #node전체 탐색이 끝나면 다시 arr값으로 교체 
    return node.count(target) #원하는 target 값이 몇개 있는지 카운트 넘겨줌