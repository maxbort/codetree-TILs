import sys

input = sys.stdin.readline

n,t = map(int,input().split())

x,y,d = map(str,input().rstrip().split())

x,y = int(x)-1,int(y)-1

for _ in range(t):
    if y < 0:
        d = 'R'
        y = 1
        continue
    elif y > n-1:
        d = 'L'
        y = n-2
        continue
    elif x < 0:
        d = 'U'
        x = 1
        continue
    elif x > n-1:
        d = 'D'
        x = n-2
        continue


    if d == 'L':
        y -= 1
    elif d == 'R':
        y += 1
    elif d == 'U':
        x += 1
    elif d == 'D':
        x -= 1
    
print(x+1,y+1)