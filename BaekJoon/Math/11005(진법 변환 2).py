# my solution
def to(n, m):
    result = ''
    while n > 0:
        n, r = n//m, n%m
        r = str(r) if r <= 9 else chr(r-10+ord('A'))
        result = r+result
    return result

n, m = map(int, input().split())
print(to(n,m))

# another solution
tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ''
while n > 0:
    answer += str(tmp[n%m])
    n //= m
print(answer[::-1])