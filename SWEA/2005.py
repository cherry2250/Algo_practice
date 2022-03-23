T = int(input()) #파스칼 삼각형 / 11의 거듭제곱
for tc in range(1, T+1):
    num = int(input())
    for n in range(num):
        a = ' '.join(map(str, str(11**n)))
        print(f'#{tc} {a}')