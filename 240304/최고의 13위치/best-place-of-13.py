import sys

input = sys.stdin.readline

n = int(input())

tile = []
for _ in range(n):
    tile.append(list(map(int,input().split())))

answer = 0
for i in range(n):
    tmp = 0
    for j in range(n-2):
        for k in range(3):
            if tile[i][j+k] == 1:
                tmp += 1
    answer = max(answer,tmp)
print(answer)