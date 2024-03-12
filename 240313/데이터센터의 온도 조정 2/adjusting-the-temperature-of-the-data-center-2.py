import sys

input = sys.stdin.readline

n,c,g,h = map(int,input().split())

temper = []

max_temp = 0
for _ in range(n):
    a,b = map(int,input().split())
    max_temp = max(max_temp,b)
    temper.append([a,b])

answer = 0
for i in range(max_temp+2):
    tmp = 0
    for ta,tb in temper:
        if i < ta:
            tmp += c
        elif ta <= i <= tb:
            tmp += g
        else:
            tmp += h
    answer = max(answer,tmp)

print(answer)