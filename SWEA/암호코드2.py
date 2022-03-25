decode = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
 
def extension_check(arr):
    target = []
    while len(arr) >= 56:
        r_first = arr.rfind('1')
        if r_first == -1:
            break
        line = arr.split('0')
        line = list(map(len,[i for i in line if i]))[-16:]
        minn, maxx = min(line), max(line)
        for i in range(minn, 0, -1):
            if not minn % i and not maxx % i:
                add = i
                break
        target.append((r_first, add))
        arr = arr[:(r_first - 55 * add) + 1]
    return target
 
 
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    answer, case = 0, set()
    for _ in range(n):
        new = ''
        for i in input():
            new += bin(int(i,16))[2:].zfill(4)
        check = new.rfind('1')
        if check == -1:
            continue
        else:
            for idx, times in extension_check(new):
                code_2 = new[idx - 56 * times + 1:idx + 1]
                if code_2 in case:
                    continue
                else:
                    case.add(code_2)
                target = ''
                if times != 1:
                    for i in range(0, len(code_2), times):
                        target += code_2[i]
                else:
                    target = code_2
                left, right, flag = 0, 0, 0
                for j in range(0, len(target), 7):
                    line = target[j:j+7]
                    if line not in decode:
                        flag = 1
                        break
                    else:
                        if j % 2:
                            right += decode[line]
                        else:
                            left += decode[line]
                if flag: 
                    continue
 
                answer += left + right if not (left * 3 + right) % 10 else 0
    print(f'#{tc} {answer}')