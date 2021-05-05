def solution(numbers, hand):
    answer = ''
    pad = {1:(0,0), 2:(0,1), 3:(0,2),
           4:(1,0), 5:(1,1), 6:(1,2),
           7:(2,0), 8:(2,1), 9:(2,2),
           '*':(3,0), 0:(3,1), '#':(3,2)}
    
    l = pad['*']
    r = pad['#']
    for number in numbers:
        left_flag = False
        cur_pos = pad[number]
        
        if number in [1,4,7]:
            left_flag = True
        elif number in [3,6,9]:
            left_flag = False
        else:
            x = cur_pos[0]
            y = cur_pos[1]

            lx = l[0]; ly = l[1]
            rx = r[0]; ry = r[1]
            ld = abs(lx-x) + abs(ly-y)
            rd = abs(rx-x) + abs(ry-y)
        
            if ld < rd:
                left_flag = True
            elif ld > rd:
                left_flag = False
            elif hand == "left":
                left_flag = True
        
        if left_flag:
            l = cur_pos
            answer += 'L'
        else:
            r = cur_pos
            answer += 'R'
        
    return answer