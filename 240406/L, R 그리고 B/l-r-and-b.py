import sys
from collections import deque

input = sys.stdin.readline

graph = [list(map(str,input().rstrip())) for _ in range(10)]
startx,starty = 0,0
for i in range(10):
    for j in range(10):
        if graph[i][j] == 'L':
            startx,starty = i,j
        elif graph[i][j] == 'B':
            endx,endy = i,j

dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = float('inf')
visited = [[False for _ in range(10)] for _ in range(10)]
q = deque()
q.append((startx,starty,0))
visited[startx][starty] = True
while q:
    x,y,cnt = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 10 and 0 <= ny < 10 and not graph[nx][ny] == 'R' and not visited[nx][ny]:
            if graph[nx][ny] == 'B':
                answer = min(answer,cnt)
            visited[nx][ny] = True
            q.append((nx,ny,cnt+1))
print(answer)