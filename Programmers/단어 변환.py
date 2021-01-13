res = []
answer = 0

def solution(begin, target, words):
    def check(cur, word):
        res = 0
        for char1, char2 in zip(cur, word):
            if char1 != char2:
                res += 1

        if res == 1:
            return True
        else:
            return False

    def dfs(cur_word, words):
        global answer

        if cur_word == target:
            global res
            res.append(answer)
            return

        for next_word in words:
            if check(cur_word, next_word):
                words.remove(cur_word)
                answer += 1
                dfs(next_word, words)
                words.append(cur_word)
                answer -= 1
        return 

    for word in words:
        if check(begin, word):
            global answer 
            answer += 1
            dfs(word, words)

    if res == []:
        return 0
    else:
        return min(res)

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
res = solution(begin, target, words)
print(res)


'''
다른 풀이
from collections import deque

def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)
'''