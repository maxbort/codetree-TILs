n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

boomCnt = sum(sum(row) for row in arr)
site = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            site.append((i,j))


shape1 = [(-2,0),(-1,0),(1,0),(2,0)]
shape2 = [(0,-1),(-1,0),(1,0),(0,1)]
shape3 = [(-1,1),(-1,-1),(1,1),(1,-1)]

temp = []
max_val = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def getSize():

    visited = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    for num, x, y in temp:
        visited[x][y] = 1

        if num == 1:
            for dx,dy in shape1:
                nx,ny = x + dx, y + dy
                if not in_range(nx,ny):
                    continue
                visited[nx][ny] = 1
        elif num == 2:
            for dx,dy in shape2:
                nx,ny = x + dx, y + dy
                if not in_range(nx,ny):
                    continue
                visited[nx][ny] = 1
        elif num == 3:
            for dx,dy in shape3:
                nx,ny = x + dx, y + dy
                if not in_range(nx,ny):
                    continue
                visited[nx][ny] = 1
    
    return sum(sum(i) for i in visited)



def choose(cnt):
    global max_val

    if cnt == boomCnt:
        max_val = max(max_val, getSize())
        return
    
    
    for i in range(1,4):
        for x,y in site:
            temp.append((i, x, y))
            choose(cnt + 1)
            temp.pop()

choose(0)
print(max_val)