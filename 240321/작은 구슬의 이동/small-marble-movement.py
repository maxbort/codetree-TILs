import sys

input = sys.stdin.readline

n,t = map(int,input().split())

x,y,d = map(str,input().rstrip().split())

x,y = int(x),int(y)

cnt = 0
for _ in range(t):
    cnt += 1
    if y == 1 and d == 'L':
        d = 'R'
        continue
    elif y == n and d == 'R':
        d = 'L'
        continue
    elif x == 1 and d == 'U':
        d = 'D'
        continue
    elif x == n and d == 'D':
        d = 'U'
        continue


    if d == 'L':
        y -= 1
    elif d == 'R':
        y += 1
    elif d == 'U':
        x -= 1
    elif d == 'D':
        x += 1
    
print(x,y)