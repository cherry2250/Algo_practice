#몫과 나머지 출력하기

T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    for item in arr :
        a = int((int(arr[0]) / int(arr[1])))
        b = (int(arr[0]) % int(arr[1]))
    print(f'#{test_case} {a} {b}')