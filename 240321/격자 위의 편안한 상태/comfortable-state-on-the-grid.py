import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [[0 for _ in range(n)] for _ in range(n)]

fill = [list(map(int,input().split())) for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for x,y in fill:
    x,y = x-1,y-1
    graph[x][y] = 1

    check = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1:
                check += 1
    if check == 3:
        print(1)
    else:
        print(0)