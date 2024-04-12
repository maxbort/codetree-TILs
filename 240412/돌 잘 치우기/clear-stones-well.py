import sys
from collections import deque

input = sys.stdin.readline

n,k,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

start_point = [list(map(int,input().split())) for _ in range(k)]
visited = [[False for _ in range(n)] for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()
answer = 0


stone_idx = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            stone_idx.append((i,j))

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def canGo(x,y):
    return inRange(x,y) and not graph[x][y] and not visited[x][y]


def bfs():
    for start in start_point:
        q.append(start)
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if canGo(nx,ny):
                q.append((nx,ny))
                visited[nx][ny] = True

def calc():
    bfs()
    cnt = 0
    for i in visited:
        for j in i:
            if j:
                cnt += 1
    return cnt


def findMax(moveList):
    global answer
    if len(moveList) == m:
        for ix,iy in moveList:
            graph[ix][iy] = 0
        answer = max(answer,calc())
        return

    for ix,iy in stone_idx:
        if (ix,iy) in moveList:
            continue
        moveList.append((ix,iy))
        findMax(moveList)
        moveList.pop()

findMax([])
print(answer)