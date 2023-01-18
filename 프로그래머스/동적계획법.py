def solution(triangle):
    n = len(triangle)
    dp = [[0] * n for _ in range(n)] #누적합을 더해줄 dp 배열 생성
    start = triangle[0][0]
    dp[0][0] = start #첫 번째값은 넣어줌 -> 아래로 내려가면서 덧셈 
    
    #최대값 구하기
    for i in range(0, n-1): #dp[0][0]이 채워졌어도 다음 값을 구하기 위해 0부터 시작
        for j in range(len(triangle[i])):
             #갈 수 있는 방향 : 아래(i+1)왼쪽(j)와 아래(i+1)오른쪽(j+1)밖에 없음
             #이미 저장된 값과 새로운 값을 더한 것 중에 큰 값을 찾는다
             dp[i+1][j] = max(dp[i+1][j], dp[i][j]+triangle[i+1][j])
             dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+triangle[i+1][j+1])
    #맨 마지막줄 누적합 중에서 가장 큰 값을 찾으면 정답
    ans = max(dp[-1])
    return ans
