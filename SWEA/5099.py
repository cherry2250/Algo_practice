T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int,input().split()))
    list_a = [] #번호
    for i in range(M):
        list_a.append(i)
    queue = list_a[0:N] # 피자번호로 돌리기(화덕큐) (삭제,삽입)

    while len(queue) != 1: # 마지막 남은게 한 개가 될 때까지
        if arr[queue[0]] != 1:  # 치즈 0 으로 안 한 것은...1//2한게 0인지아닌지 
            arr[queue[0]] = arr[queue[0]] // 2 
            queue.append(queue.pop(0)) # 화덕큐 앞에 있는게 뽑아 뒤로 이동하기
        else: # 치즈량이 1이라면, //2 된게 => 어차피 0일테니, 바로 교체
            queue.pop(0)
            if N != M: # M개를 다 넣을 때까지 
                queue.append(list_a[N]) # pop한 자리에, 넣고 뒤로 돌린다 = 뒤로 바로 삽입 
                N += 1 # 다음넣을차례
 
    ans = queue[0] + 1
    print(f'#{tc} {ans}')