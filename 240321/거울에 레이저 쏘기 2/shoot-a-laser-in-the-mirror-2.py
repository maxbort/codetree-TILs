import sys

input = sys.stdin.readline

n = int(input())

mirror = [list(input().rstrip()) for _ in range(n)]

point = int(input())

x,y = 0,0
d = 0
if point // n == 0:
    x,y = 0,point-1
    d = 0
elif point //n == 1:
    x, y = point % n -1 , n-1
    d = 1
elif point//n == 2:
    x,y = n-1, n - (point - 2*n)
    d = 2
else:
    x,y = point % (3*n),0
    d = 3

#남서북동
dx = [1,0,-1,0]
dy = [0,-1,0,1]

answer = 0
while 0 <= x < n and 0 <= y < n:
    answer += 1
    if mirror[x][y] == '/' or mirror[x][y] == '//':
        if d == 0:
            d = 1
        elif d == 1:
            d = 0
        elif d == 2:
            d = 3
        elif d == 3:
            d = 2
        x += dx[d]
        y += dy[d]
    elif mirror[x][y] == '\\':
        if d == 0:
            d = 3
        elif d == 3:
            d = 0
        elif d == 1:
            d = 2
        elif d == 2:
            d = 1
        x += dx[d]
        y += dy[d] 


print(answer)