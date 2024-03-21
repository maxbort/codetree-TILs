import sys

input = sys.stdin.readline

command = list(input().rstrip())

dx = [-1,0,1,0]
dy = [0,1,0,-1] # 북동남서

d = 0
x,y = 0,0
answer = 0
for com in command:
    answer += 1
    if com == 'F':
        x += dx[d]
        y += dy[d]
        if x == 0 and y == 0:
            print(answer)
            sys.exit()
    elif com == 'L':
        if d == 0:
            d = 3
        else:
            d -= 1
    elif com == 'R':
        d = (d+1)%4
    
    
print(-1)