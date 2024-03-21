import sys

input = sys.stdin.readline

n, m = map(int,input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]

d = 0

# 남동북서
dx = [1,0,-1,0]
dy = [0,1,0,-1]

x,y = 0,0
cnt = 1

while cnt <= n*m:
    if graph[x][y] == 0:
        graph[x][y] = cnt
    cnt += 1
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] == 0:
            x,y = nx,ny
        else:
            d = (d+1)%4
            x = x + dx[d]
            y = y + dy[d]
            
    else:
        d = (d+1)%4
        x = x + dx[d]
        y = y + dy[d]

for i in graph:
    for j in i:
        print(j, end = ' ')
    print()