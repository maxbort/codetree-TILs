import sys

input = sys.stdin.readline

pan_len = 19
pan = []
dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy= [-1, 0, 1, -1, 0, 1, -1, 1]
for _ in range(pan_len):
    pan.append(list(map(int,input().split())))

for i in range(pan_len):
    for j in range(pan_len):

        if pan[i][j] != 0:
            cnt = 1
            for k in range(8):
                x, y = i,j
                while True:
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < pan_len and 0 <= ny < pan_len and pan[nx][ny] == pan[i][j]:
                        cnt += 1
                        x, y = nx,ny
                    else:
                        break
                if cnt == 5:
                    print(pan[i][j])
                    print(i+ 2*dx[k] + 1, j+ 2*dy[k] + 1)
                    sys.exit()
print(0)