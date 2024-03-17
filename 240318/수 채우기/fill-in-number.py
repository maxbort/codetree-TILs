import sys

input = sys.stdin.readline

n = str(input())

coin = [5,2]

answer = 0

if n[-1] == '1' or n[-1] == '3':
    if n[-1] == '1':
        n = int(n) - 21
        answer += 6
        for i in coin:
            a = n //i
            answer += a
            n -= a * i
    else:
        n = int(n) - 13
        answer += 5
        for i in coin:
            a = n //i
            answer += a
            n -= a * i

else:
    n = int(n)
    for i in coin:
        a = n //i
        answer += a
        n -= a * i

if n == 0:
    print(answer)
else:
    print(-1)