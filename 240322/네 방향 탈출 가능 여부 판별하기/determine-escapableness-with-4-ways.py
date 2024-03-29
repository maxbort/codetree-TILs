import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()
q.append((0,0))

visited = [[False for _ in range(m)] for _ in range(n)]

visited[0][0] = True
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny] :
            visited[nx][ny] = True
            q.append((nx,ny))
    if visited[-1][-1]:
        break
if visited[-1][-1]:
    print(1)
else:
    print(0)