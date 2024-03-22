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
start_x,start_y = start_x-1,start_y-1

q.append((start_x,start_y))

visited[start_x][start_y] = True
real_visited = [[False for _ in range(n)] for _ in range((n))]

for _ in range(k):
    visited = [[False for _ in range(n)] for _ in range(n)]
    check = graph[start_x][start_y]
    visited[start_x][start_y] = True
    real_visited[start_x][start_y] = True
    tmp = []
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] < check and not visited[nx][ny] and not real_visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
                tmp.append([graph[nx][ny],nx,ny])
    if not tmp:
        print(x+1,y+1)
        sys.exit()
    
    tmp.sort(key=lambda x: (-x[0],x[1],x[2]))
                   
    start_x,start_y = tmp[0][1],tmp[0][2]
    q.append((start_x,start_y))
    
print(start_x+1,start_y+1)