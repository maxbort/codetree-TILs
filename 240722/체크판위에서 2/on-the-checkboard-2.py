from collections import deque

r,c = map(int,input().split())

arr = [
    list(input().split())
    for _ in range(r)
]

d = [
    [0 for _ in range(c)]
    for _ in range(r)
]

q = deque()
q.append((0,0))
cnt = 0

while q:
    x,y = q.popleft()

    if arr[0][0] == arr[r-1][c-1]:
        cnt = 0
        break

    for i in range(x+1, r-2):
        for j in range(y+1, c-2):
            if arr[i][j] != arr[x][y]:
                for a in range(i+1, r-1):
                    for b in range(j+1, c-1):
                        if arr[x][y] == arr[a][b]:
                            cnt += 1



print(cnt)