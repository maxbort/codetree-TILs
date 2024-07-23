n,m = map(int,input().split())

arr = [
    list(input())
    for _ in range(n)
]

cnt = 0

dxs,dys = [0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1] 

def in_range(x,y):
    return 0<=x<n and 0<=y<m


for i in range(n):
    for j in range(m):
        if arr[i][j] == "L":
            for dx, dy in zip(dxs,dys):
                flag = True

                for k in range(1,3):
            
                    if not in_range(i + dx * k, j + dy * k) or arr[i + dx * k][j + dy * k] != 'E':
                        flag = False
                        break
        
                if flag:
                    cnt += 1
print(cnt)