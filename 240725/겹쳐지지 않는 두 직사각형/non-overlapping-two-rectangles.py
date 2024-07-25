import sys

n,m = map(int,input().split())

max_val = -sys.maxsize

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [0] * m
    for _ in range(n)
]

def init_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0

def overlap():
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                return True
    return False

def draw(x1,y1,x2,y2,x3,y3,x4,y4):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            visited[i][j] += 1
    for i in range(x3,x4+1):
        for j in range(y3,y4+1):
            visited[i][j] += 1

def check_overlap(x1,y1,x2,y2,x3,y3,x4,y4):
    init_visited()
    draw(x1,y1,x2,y2,x3,y3,x4,y4)
    return overlap()

def sum_rect(x1,y1,x2,y2):
    cnt = 0
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            cnt += arr[i][j]
    return cnt

def total_sum_rect(x1,y1,x2,y2):
    max_val = -sys.maxsize

    for i in range(n):
        for j in range(m):
            for x in range(i,n):
                for y in range(j,m):
                    if not check_overlap(x1,y1,x2,y2,i,j,x,y):
                        max_val = max(max_val, sum_rect(x1,y1,x2,y2) + sum_rect(i,j,x,y))
    return max_val

for i in range(n):
    for j in range(m):
        for x in range(i,n):
            for y in range(j,m):
                max_val = max(max_val, total_sum_rect(i,j,x,y))
print(max_val)