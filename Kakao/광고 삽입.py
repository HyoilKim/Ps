def solution(play_time, adv_time, logs):
    def time_to_sec(time):
        t = time.split(':')
        return sum([x*y for x, y in zip(map(int, time.split(':')), [3600, 60, 1])])
    def sec_to_time(sec):
        h, m = divmod(sec, 3600)
        m, s = divmod(m, 60)
        return '{:02d}:{:02d}:{:02d}'.format(h,m,s)

    adv_sec = time_to_sec(adv_time)
    play_sec = time_to_sec(play_time)
    start_times = []
    end_times = []

    for log in logs:
        s, e = log.split('-')
        start_times.append(time_to_sec(s))
        end_times.append(time_to_sec(e))
    start_times.sort()
    end_times.sort()
    
    viewers = [0]*play_sec
    viewer = si = ei = 0
    for i in range(play_sec):
        while si < len(start_times) and start_times[si] <= i: 
            print(i, '+')
            si += 1
            viewer += 1
        while ei < len(end_times) and end_times[ei] <= i:
            print(i ,'-')
            ei += 1
            viewer -= 1
        viewers[i] = viewer
        
    answer = max_viewer = 0
    total = sum(viewers[:adv_sec])
    for i in range(play_sec-adv_sec):
        if total > max_viewer:
            max_viewer = max(max_viewer, total)
            answer = i
        total -= viewers[i]
        total += viewers[i+adv_sec]

    return sec_to_time(answer)