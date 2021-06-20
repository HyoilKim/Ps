import sys
input = sys.stdin.readline

def solution(camels):    
    if len(camels) <= 2:
        return camels[-1]
    elif len(camels) == 3:
        return sum(camels)
    else:
        return solution(camels[:-2]) + min(2*camels[0]+camels[-1]+camels[-2], \
                                            camels[0]+2*camels[1]+camels[-1])
        
def main():
    tc = int(input())
    for i in range(tc):
        n = int(input())
        camels = list(map(int, input().split()))
        camels.sort()
        times = solution(camels)
        print('#{0} {1}'.format(i+1, times))

main()