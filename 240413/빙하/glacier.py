import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]



answer = 0
check = True
while check:
    visited = [[False for _ in range(m)] for _ in range(n)]

    ice_list = []
    q = deque()
    flag = True
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and not visited[i][j]:
                q.append((i,j))
                visited[i][j] = True
                flag= False
                break
        if not flag:
            break
     

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                else:
                    if (nx,ny) not in ice_list:
                        ice_list.append((nx,ny))
    answer2 = 0
    while ice_list:
        a,b = ice_list.pop()
        graph[a][b] = 0
        answer2 += 1

    answer += 1

    check = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                check = True
    

print(answer, answer2)