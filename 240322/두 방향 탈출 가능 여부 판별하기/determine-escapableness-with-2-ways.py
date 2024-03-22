import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]

dx = [0,1]
dy = [1,0]

def dfs(x,y,visited):
    visited[x][y] = True

    for i in range(2):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx,ny,visited)

dfs(0,0,visited)
if visited[-1][-1]:
    print(1)
else:
    print(0)