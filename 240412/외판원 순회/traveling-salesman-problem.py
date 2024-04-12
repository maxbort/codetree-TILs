import sys

input = sys.stdin.readline

n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

visited = [False for _ in range(n)]
answer = float('inf')

def findMin(cnt,cur,tmp):
    global answer
    if cnt == n-1:
        if graph[cur][0] == 0:
            return
        tmp += graph[cur][0]
        answer = min(answer,tmp)
        return
   
    for i in range(1,n):
        if visited[i]:
            continue
        if graph[cur][i] == 0:
            continue
        tmp += graph[cur][i]
        visited[i] = True
        findMin(cnt+1,i,tmp)
        tmp -= graph[cur][i]
        visited[i] = False

findMin(0,0,0)
print(answer)