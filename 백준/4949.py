#균형잡힌 세상
while True:
    str = input()
    ans = []
    if str == '.' :
        break
    for i in str:
        if i == '(' or i == '[':
            ans.append(i)
        elif i == ']':
            if ans and ans[-1] == '[':
                ans.pop()
            else:
                ans.append('X')
                break
        elif i == ')':
            if ans and ans[-1] == '(':
                ans.pop()
            else:
                ans.append('X')
                break
        else:
            continue
                
    if len(ans) != 0 :
        print('no')
    else:
        print('yes')