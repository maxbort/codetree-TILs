import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
start_x,start_y = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False for _ in range(n)] for _ in range(n)]


q = deque()
check = graph[start_x-1][start_y-1]
q.append((start_x-1,start_y-1))

visited[start_x-1][start_y-1] = True

for _ in range(k):
    x, y = q.popleft()
    a,b = n,n
    tmp = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if graph[nx][ny] < check:
                tmp.append((graph[nx][ny],nx,ny))
    tmp.sort(key=lambda x : (-x[0], x[1],x[2]))
    
    if not tmp:
        print(x+1,y+1)
        sys.exit()
    a,b = tmp[0][1],tmp[0][2]
    
    visited[a][b] = True
    q.append((a,b))

a,b = q.popleft()
print(a+1,b+1)