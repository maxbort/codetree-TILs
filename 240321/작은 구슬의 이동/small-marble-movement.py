import sys

input = sys.stdin.readline

n,t = map(int,input().split())

graph = [[0 for _ in range(n)] for _ in range(n)]


x,y,h = map(str,input().rstrip().split())

x,y = int(x),int(y)


for _ in range(t):
    if y == 0:
        h = 'R'
        y = 1
    elif y == n:
        h = 'L'
        y = n-1
    elif x == 0:
        h = 'D'
        x = 1
    elif x == n:
        h = 'U'
        x = n-1
    if h == 'L':
        y -= 1
    elif h == 'R':
        y += 1
    elif h == 'D':
        x -= 1
    else:
        x += 1
    
    
    
        

print(x,y)