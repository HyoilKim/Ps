def solution(code, day, data):
    answer = []
    info = [x.split() for x in data]
    for i in info:
        _price = i[0].split('=')
        _code = i[1].split('=')
        _day = i[2].split('=')
        if _code[1] == code and _day[1][:8] == day:
            answer.append((_day[1][-2:], int(_price[1])))
    answer.sort(key = lambda x: x[0])
    return [i[1] for i in answer]