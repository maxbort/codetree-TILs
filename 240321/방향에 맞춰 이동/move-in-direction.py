import sys

input = sys.stdin.readline

n = int(input())

command = [list(input().rstrip().split()) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]

x,y = 0,0
for com,cnt in command:
    if com == 'E':
        x += int(cnt) * dx[0]
    elif com == 'W':
        x += int(cnt) * dx[1]
    elif com == 'S':
        y += int(cnt) * dy[2]
    else:
        y+= int(cnt) * dy[3]


print(x,y)