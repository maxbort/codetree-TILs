import sys

input = sys.stdin.readline

n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

visited = [False for _ in range(n)]

answer = 0
def findMax(cur,tmp,visited):
    global answer
    if cur == n:
        answer = max(answer,tmp)
        return

    for i in range(n):
        if visited[i]:
            continue
        
        tmp += graph[cur][i]
        visited[i] = True

        findMax(cur+1,tmp,visited)

        tmp -= graph[cur][i]
        visited[i] = False

findMax(0,0,visited)
print(answer)