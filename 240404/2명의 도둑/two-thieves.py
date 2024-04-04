import sys

input = sys.stdin.readline

n,m,c = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]


answer = 0

def calValue(x,y):
    value = 0
    candi = graph[x][y:y+m]
    candi.sort(reverse=True)
    limit = 0
    for i in candi:
        limit += i
        if limit <= c:
            value += i*i
    return value

def findMax():
    if x1 == x2:
        if y1 < n-m:
            answer = max(answer)


for i in range(n):
    for j in range(n-m):
        for k in range(n):
            for l in range(n-m):
                if i == k:
                    if i < n-2*m:
                        answer = max(answer,calValue(i,j) + calValue(k,l))
                    else:
                        break
                else:
                    answer = max(answer,calValue(i,j) + calValue(k,l))

print(answer)