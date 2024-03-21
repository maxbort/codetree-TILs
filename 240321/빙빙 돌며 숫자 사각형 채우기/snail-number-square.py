import sys

input = sys.stdin.readline

m,n = map(int,input().split())

graph = [[0 for _ in range(n)] for _ in range(m)]

cnt = 1
d = 0
x,y = 0,0
dx = [0,1,0,-1]
dy = [1,0,-1,0]

while cnt < m*n+1:
    if graph[x][y] == 0:
        graph[x][y] = cnt
        cnt += 1
    
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
        x += dx[d]
        y += dy[d]

    else:
        d = (d+1)%4

for i in graph:
    for j in i:
        print(j, end=' ')
    print()