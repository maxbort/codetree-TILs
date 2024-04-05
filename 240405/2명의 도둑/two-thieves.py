import sys

input = sys.stdin.readline

n,m,c = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

def calcValue(tmp):
    value = 0
    return sum(i*i for i in tmp)
answer = 0

def findMax(x,y,x2,y2,cnt,tmp,tmp2):
    global answer
    if sum(tmp) > c:
        tmp.pop()
        answer = max(answer,calcValue(tmp2)+calcValue(tmp))
        return
    
    if cnt == m-1:        
        answer = max(answer,calcValue(tmp2)+calcValue(tmp))
        return 
    if sum(tmp2) > c:
        tmp2.pop()
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


for i in range(n):
    for j in range(n-m+1):
        for k in range(n):
            for l in range(n-m+1):
                if i == k:
                    z = l+j+m
                    if z > n-m+1:
                        break
                    findMax(i,j,k,l,0,[],[])
                else:
                    findMax(i,j,k,l,0,[],[])

print(answer)