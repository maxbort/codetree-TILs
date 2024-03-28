import sys

input = sys.stdin.readline

n = int(input())

graph = [[0 for _ in range(n)] for _ in range(n)]
field = [[False for _ in range(n)] for _ in range(n)]
answer = 0



b_list = []

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def do_bomb(x,y,bomb_num):
    bomb_list = [[],
    [(0,0),(0,1),(0,2),(0,-1),(0,-2)], 
    [(0,0),(1,0),(0,1),(0,-1),(-1,0)],
    [(0,0),(1,1),(-1,1),(-1,-1),(1,-1)]
    ]

    for i in range(5):
        dx,dy = bomb_list[bomb_num][i];
        nx,ny = x+dx, y+dy
        if in_range(nx,ny):
            field[nx][ny] = True


def count():
    for i in range(n):
        for j in range(n):
            field[i][j] = False

    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                do_bomb(i,j,graph[i][j])

    cnt = 0
    for i in range(n):
        for j in range(n):
            if field[i][j]:
                cnt += 1
    
    return cnt

def find_max(cnt):
    global answer

    if cnt == len(b_list):
        answer = max(answer,count())
        return

    for i in range(1,4):
        x,y = b_list[cnt]

        graph[x][y] = i
        find_max(cnt+1)
        graph[x][y] = 0


for i in range(n):
    input_str = list(map(int,input().split()))
    for j,point in enumerate(input_str):
        if point:
            b_list.append((i,j))

find_max(0)
print(answer)