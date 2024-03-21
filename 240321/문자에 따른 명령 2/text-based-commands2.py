import sys

input = sys.stdin.readline

command = list(input().rstrip())

dx = [-1,0,1,0]
dy = [0,-1,0,1] 

# 시작 방향은 북쪽
dir = 3
x,y = 0,0
for com in command:
    if com == 'L':
        dir = (dir+1) %4
    elif com == 'R':
        if dir == 0:
            dir = 3
        else:
            dir -= 1
    else:
        x += dx[dir]
        y += dy[dir]

print(x,y)