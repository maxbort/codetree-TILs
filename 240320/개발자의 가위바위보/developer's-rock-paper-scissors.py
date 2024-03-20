import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

versus = [list(map(int,input().split())) for _ in range(n)]

rsp = ['r','s','p']
rsp_p = list(permutations(rsp))

def result(a,b):
    if a == 'r':
        if b == 's':
            return True
    elif a == 's':
        if b == 'p':
            return True
    elif a == 'p':
        if b=='r':
            return True
    return False
answer = 0
for i in rsp_p:
    tmp = 0
    for j in versus:
        if result(i[j[0]-1],i[j[1]-1]):
            tmp += 1

    answer = max(answer,tmp)
print(answer)