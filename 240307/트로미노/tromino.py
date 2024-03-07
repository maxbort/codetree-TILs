import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

move_type = [[[0,-1], [1,0],[0,0]], [[-1,0], [0,-1],[0,0]], [[1,0],[0,1],[0,0]], [[-1,0],[0,1],[0,0]]]
answer = 0
# 가로 or 세로 3줄 블럭 먼저
for i in range(n):
    for j in range(m-2):
        tmp = 0
        for k in range(3):
            tmp += graph[i][j+k]
        answer = max(answer,tmp)

for i in range(n-2):
    for j in range(m):
        tmp = 0
        for k in range(3):
            tmp += graph[i+k][j]
        answer = max(answer,tmp)

for i in range(n):
    for j in range(m):
        for move in move_type:
            tmp = 0
            for do_move in move:
                if 0 <= i+do_move[0] < n and 0 <= j+do_move[1]<m:
                    tmp += graph[i+do_move[0]][j+do_move[1]]
            answer = max(answer,tmp)

print(answer)