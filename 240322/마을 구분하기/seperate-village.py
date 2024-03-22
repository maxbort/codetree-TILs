import sys

input = sys.stdin.readline

n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

danji = []

visited = [[False for _ in range(n)] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

tmp = []
def dfs(x,y,visited):
    visited[x][y] = True
    tmp.append((x,y))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx,ny,visited)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            tmp = []
            dfs(i,j,visited)
            danji.append(tmp)

print(len(danji))
danji.sort(key=lambda x : len(x))
for i in danji:
    print(len(i))