import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

line_list = [list(map(int,input().split())) for _ in range(n)]
max_xy = 11
q = deque(line_list)


def xxx(i,j,k,q):
    while q:            
        x,y = q.popleft()
        if x == i or x == j or x == k:
            continue
        else:
            return False
    return True
def yyy(i,j,k,q):
    while q:            
        x,y = q.popleft()
        if y == i or y == j or y == k:
            continue
        else:
            return False
    return True
def xxy(i,j,k,q):
    while q:            
        x,y = q.popleft()
        if x == i or x == j or y == k:
            continue
        else:
            return False
    return True
def xyy(i,j,k,q):
    while q:            
        x,y = q.popleft()
        if y == i or y == j or x == k:
            continue
        else:
            return False
    return True
# xxx, yyy

a,b,c,d = False, False, False, False
for i in range(max_xy-2):
    for j in range(i+1,max_xy):
        for k in range(j+1,max_xy):
            a = xxx(i,j,k,q)
            b = xxx(i,j,k,q)
            if a or b:
                print(1)
                sys.exit()

# xxy, xxy
for i in range(max_xy-1):
    for j in range(i+1,max_xy):
        for k in range(max_xy):
            c = xxy(i,j,k,q)
            d = xyy(i,j,k,q)
            if c or d:
                print(1)
                sys.exit()