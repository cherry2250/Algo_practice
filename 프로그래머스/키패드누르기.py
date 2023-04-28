def solution(numbers, hand):
    answer = ''
    left, right = [1, 4, 7], [3, 6, 9]
    n_left, n_right = 0, 0
    right_hand = ['#']
    left_hand = ['*']
    for i in numbers:
        if i in left:
            answer += 'L'
            n_left = i
            left_hand.append(n_left)
        elif i in right:
            answer += 'R'
            n_right = i
            right_hand.append(n_right)
        else:
            if abs(i-n_left) > abs(i-n_right):
                answer += 'R'
                n_right = i
                right_hand.append(n_right)
            elif abs(i-n_left) < abs(i-n_right):
                answer += 'L'
                n_left = i
                left_hand.append(n_left)
            else :
                print('여기옴', hand)
                if hand == 'right':
                    answer += 'R'
                    n_right = i
                    right_hand.append(n_right)
                else :
                    answer += 'L'
                    n_left = i            
                    left_hand.append(n_left)
    print(right_hand, left_hand)   
    return answer