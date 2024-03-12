import sys

input = sys.stdin.readline

n = int(input())

simul = [list(map(int,input().split())) for _ in range(n)]
answer = 0


for i in range(3):
    tmp = 0
    cups = [0,0,0]
    cups[i] = 1
    for a,b,c in simul:
        cups[a-1], cups[b-1] = cups[b-1], cups[a-1]
        if cups[c-1] == 1:
            tmp += 1
    answer = max(tmp,answer) 
print(answer)