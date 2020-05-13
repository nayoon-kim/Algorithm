keypad = {1:0, 2:1, 3:2,4:3, 5:4, 6:5,7:6, 8:7, 9:8, '*':9, 0:10, '#':11}
distance_2 = [1, 0, 1, 2, 1, 2, 3, 2, 3, 4, 3, 4]
distance_5 = [2, 1, 2, 1, 0, 1, 2, 1, 2, 3, 2, 3]
distance_8 = [3, 2, 3, 2, 1, 2, 1, 0, 1, 2, 1, 2]
distance_0 = [4, 3, 4, 3, 2, 3, 2, 1, 2, 1, 0, 1]

def solution(numbers, hand):
    answer = ''
    key_left = '*'
    key_right = '#'

    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            key_left = i
            answer += 'L'
        elif i == 3 or i == 6 or i == 9:
            key_right = i
            answer += 'R'
        elif i == 2 :
            if distance_2[keypad[key_left]] < distance_2[keypad[key_right]]:
                key_left = i
                answer += 'L'
            elif distance_2[keypad[key_left]] > distance_2[keypad[key_right]]:
                key_right = i
                answer += 'R'
            else:
                if hand == 'left':
                    key_left = i
                    answer += 'L'
                else:
                    key_right = i
                    answer += 'R'
        elif i == 5 :
            if distance_5[keypad[key_left]] < distance_5[keypad[key_right]]:
                key_left = i
                answer += 'L'
            elif distance_5[keypad[key_left]] > distance_5[keypad[key_right]]:
                key_right = i
                answer += 'R'
            else:
                if hand == 'left':
                    key_left = i
                    answer += 'L'
                else:
                    key_right = i
                    answer += 'R'
        elif i == 8:
            if distance_8[keypad[key_left]] < distance_8[keypad[key_right]]:
                key_left = i
                answer += 'L'
            elif distance_8[keypad[key_left]] > distance_8[keypad[key_right]]:
                key_right = i
                answer += 'R'
            else:
                if hand == 'left':
                    key_left = i
                    answer += 'L'
                else:
                    key_right = i
                    answer += 'R'
        elif i == 0:
            if distance_0[keypad[key_left]] < distance_0[keypad[key_right]]:
                key_left = i
                answer += 'L'
            elif distance_0[keypad[key_left]] > distance_0[keypad[key_right]]:
                key_right = i
                answer += 'R'
            else:
                if hand == 'left':
                    key_left = i
                    answer += 'L'
                else:
                    key_right = i
                    answer += 'R'

    return answer
