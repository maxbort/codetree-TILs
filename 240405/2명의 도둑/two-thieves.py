import sys

input = sys.stdin.readline

n,m,c = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

def calcValue(tmp):
    return sum(i*i for i in tmp)

answer = 0

def findMax(x,y,x2,y2,cnt,tmp,tmp2):
    global answer
    if sum(tmp) > c or sum(tmp2) > c:
        return
    if cnt == m:
        answer = max(answer,calcValue(tmp2)+calcValue(tmp))
        return 
    
    tmp.append(graph[x][y+cnt])
    findMax(x,y,x2,y2,cnt+1,tmp,tmp2)
    tmp2.append(graph[x2][y2+cnt])
    findMax(x,y,x2,y2,cnt+1,tmp,tmp2)
    tmp.pop()
    findMax(x,y,x2,y2,cnt+1,tmp,tmp2)
    tmp2.pop()
    findMax(x,y,x2,y2,cnt+1,tmp,tmp2)

for x in range(n):
    for y in range(n-m+1):
        for x2 in range(n):
            for y2 in range(n-m+1):
                if x == x2:
                    if y+m < y2:
                        findMax(x,y,x2,y2,0,[],[])
                else:
                    findMax(x,y,x2,y2,0,[],[])

print(answer)