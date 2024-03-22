import sys 

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n+1)]

def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
    
dfs(1)

answer= 0 
for i in visited:
    if i:
        answer += 1
print(answer-1)