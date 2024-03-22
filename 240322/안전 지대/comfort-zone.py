import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,k,visited):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] > k:
            dfs(nx,ny,k,visited)
 
k =1
answer = 0
answer_k = 0
while True:
    tmp = 
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] > k and not visited[i][j]:
                tmp += 0
                dfs(i,j,k,visited)
    if answer < tmp:
        answer = tmp
        answer_k = k
    if tmp == 0:
        break
    k += 1
print(answer, answer_k)