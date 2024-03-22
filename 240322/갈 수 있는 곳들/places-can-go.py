import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
start_point = [list(map(int,input().split())) for _ in range(k)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q =deque()
visited = [[False for _ in range(n)] for _ in range(n)]
for a,b in start_point:
    q.append((a-1,b-1))
    visited[a-1][b-1] = True
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n  and graph[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True

answer = 0
for i in visited:
    for j in i:
        if j:
            answer += 1
print(answer)