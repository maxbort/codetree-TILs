import sys

input = sys.stdin.readline

a,b,c = map(int,input().split())

answer = 0

for i in range((c//a) + 1):
    for j in range((c//b) +1):
        tmp = a * i + b * j
        if answer <= tmp <= c:
            answer = max(answer,tmp)
print(answer)