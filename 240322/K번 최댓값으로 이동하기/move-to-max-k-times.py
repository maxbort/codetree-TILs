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
visited[start_x-1][start_y-1] = True
q.append((start_x-1,start_y-1))


for _ in range(k):
    x,y = q.popleft()
    a,b = n,n
    tmp = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                if graph[nx][ny] < check and tmp <= graph[nx][ny]:
                    tmp = graph[nx][ny]
                    if ny < b:
                        a,b = nx,ny
    if a == n or b == n:
        print(x,y)
        sys.exit()
    visited[a][b] = True
    q.append((a,b))
    
answer_y,answer_x = q.popleft()
print(answer_x+1,answer_y+1)