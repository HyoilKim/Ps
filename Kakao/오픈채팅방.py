def solution(record):
    id_to_name = dict()
    for i in record:
        cmd = i.split()
        if cmd[0] == 'Enter' or cmd[0] == 'Change':
            id_to_name[cmd[1]] = cmd[2]
            
    answer = []
    for i in record:
        cmd = i.split()
        msg = ''
        if cmd[0] == 'Enter':
            msg = id_to_name[cmd[1]]+'님이 들어왔습니다.'
        elif cmd[0] == 'Leave':
            msg = id_to_name[cmd[1]]+'님이 나갔습니다.'
        else:
            continue
        answer.append(msg)
        
    return answer