import sys

input = sys.stdin.readline
n,m = map(int,input().split())

#동남서북
dx = [0,1,0,-1]
dy = [1,0,-1,0]

d=0
cnt = 'A'

graph = [[0 for _ in range(m)] for _ in range(n)]

x,y = 0,0
flag = True
while flag:
    if graph[x][y] == 0:
        graph[x][y] = cnt
    flag=False
    for i in range(4):
        a = x+dx[i]
        b = y+dy[i]
        if 0 <= a < n and 0<= b < m:
            if graph[a][b] == 0:
                flag=True
                break

    if cnt == 'Z':
        cnt = 'A'
    else:
        cnt = chr(ord(cnt)+1)
    
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] == 0:
            x,y = nx,ny
        else:
            d = (d+1)%4
            x = x + dx[d]
            y = y+ dy[d]
    else:
        d = (d+1)%4
        x = x + dx[d]
        y = y+ dy[d]


for i in graph:
    for j in i:
        print(j, end=' ')
    print()