# my solution
number = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]

word = input()
time = 0
for char in word:
    time += (number[ord(char)-65])+1
print(time)

# another solution
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
a = input()
ret = 0
for i in a:
    for j in dial:
        if i in j:
            ret += dial.index(j) + 3
print(ret)