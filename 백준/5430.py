import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    fx = input()
    len_n = int(input())
    arr = input().rstrip()[1:-1].split(',')
    r_cnt = 0
    front_cnt = 0
    back_cnt = 0
    for i in fx:
        if i == 'R':
            r_cnt += 1
        elif i == 'D':
            if r_cnt % 2 == 0:
                front_cnt += 1
            else:
                back_cnt += 1
    if front_cnt + back_cnt <= len_n :
        arr = arr[front_cnt:len_n-back_cnt]
        if r_cnt % 2 == 1:
            print('[' + ','.join(arr[::-1]) + ']')
        else:
            print('[' + ','.join(arr) + ']')
    else:
        print('error')