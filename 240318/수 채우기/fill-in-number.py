import sys

input = sys.stdin.readline

n = str(input().rstrip())

coin = [5,2]

answer = 0

if len(n) > 1:
    if n[-1] == '1':
        n = int(n) - 21
        answer += 6
        for i in coin:
            a = n //i
            answer += a
            n -= a * i
    elif n[-1] == '3':
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