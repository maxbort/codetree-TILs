import sys
from itertools import permutations

input = sys.stdin.readline

k,n = map(int,input().split())

ranking = [list(map(int,input().split())) for _ in range(k)]

user = [i+1 for i in range(n)]
combi = list(permutations(user,2))
answer = 0
for a,b in combi:
    flag = True
    for game in ranking:
        if game.index(a) < game.index(b):
            flag = False
            break
    if flag:
        answer += 1

print(answer)