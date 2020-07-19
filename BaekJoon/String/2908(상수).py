a, b = (input().split(' '))
a = int(''.join(reversed(a)))
b = int(''.join(reversed(b)))

print(a) if a > b else print(b)

# 문자열 거꾸로 출력하는 다른 방법
# print(string[::-1])
# string[a:b:-1] : a인덱스 부터 b-1인덱스 까지 역순(-1)으로
