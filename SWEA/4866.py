def finding(char):
    dict_a = {'}' : '{', ')' : '('}
    ans = []
    for i in char:
        if i in ("{", "("):
            ans.append(i)
        if i in ('}', ')'):
            if ans[len(ans)-1] != dict_a[i]:
                return 0
            if not ans:
                return 0
            ans.pop()
    if ans :
        return 0
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    char = input()
    a = finding(char)
    print(f'#{tc} {a}')