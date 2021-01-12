import itertools
import sys
input = sys.stdin.readline

n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]
team_list = list(itertools.combinations([i for i in range(n)], n//2))

def team_ability(team):
    sum = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            sum += ability[team[i]][team[j]]
            sum += ability[team[j]][team[i]]
    return sum

res = float('inf')

for i in range(len(team_list)//2):
    team_start = team_list[i]
    team_link = [i for i in range(n)]
    for j in team_start:
        team_link.remove(j)
    
    score_start = team_ability(team_start)
    score_link = team_ability(team_link)
    
    sub = abs(score_start-score_link)
    if sub < res:
        res = sub

print(res)
    