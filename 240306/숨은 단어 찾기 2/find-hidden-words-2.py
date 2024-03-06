import sys

input = sys.stdin.readline

n,m = map(int,input().split())
table = []
for _ in range(n):
    table.append(list(input().rstrip()))


dx = [1,1,1,-1,-1,-1,0,0]
dy = [0,1,-1,0,1,-1,-1,1]

cnt = 0

for i in range(n):
    for j in range(m):
        if table[i][j] == 'L':
            for k in range(8):
                x, y = i,j
                flag = False
                while True:
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and table[nx][ny] == 'E':
                        if flag:
                            cnt += 1
                            flag = False
                            break
                        else:
                            flag= True
                            x,y = nx,ny
                    else:
                        break
print(cnt)