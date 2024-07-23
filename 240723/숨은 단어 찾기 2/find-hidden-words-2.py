n,m = map(int,input().split())

arr = [
    list(input())
    for _ in range(n)
]

cnt = 0

dxs,dys = [0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1] 

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def check(x,y):
    global cnt
    for dx, dy in zip(dxs,dys):
        flag = True

        for i in range(1,3):
            
            if not in_range(x + dx * i, y + dy * i) or arr[x + dx * i][y + dy * i] != 'E':
                flag = False
                break
        
        if flag:
            cnt += 1


for i in range(n):
    for j in range(m):
        if arr[i][j] == "L":
            check(i,j)
print(cnt)