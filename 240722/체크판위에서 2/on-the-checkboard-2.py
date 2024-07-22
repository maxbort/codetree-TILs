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


cnt = 0


if arr[0][0] == arr[r-1][c-1]:
    cnt = 0
else:
    for i in range(1, r-2):
        for j in range(1, c-2):
            for a in range(i+1, r-1):
                for b in range(j+1, c-1):
                    if arr[i][j] != arr[0][0] and arr[0][0] == arr[a][b]:
                        cnt += 1



print(cnt)