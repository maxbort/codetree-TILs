import sys

input = sys.stdin.readline

n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(n):
        tmp = 0
        start = graph[i][j]
        x,y = i,j
        check1 = 0
        check2 = 0
        while True:
            dx = x - 1
            dy = y + 1
            if 0 <= dx < n and 0 <= dy < n:
                if dx == 0 and dy == n-1:
                    break
                check1+= 1
                tmp += graph[dx][dy]
                x,y = dx,dy
            else:
                break

        if check1 == 0:
            continue

        while True:
            dx = x - 1
            dy = y - 1
            if 0 <= dx < n and 0 <= dy < n:
                if dx == 0 and dy == 0:
                    break
                tmp += graph[dx][dy]
                check2+= 1
                x,y = dx,dy
            else:
                break

        if check2 == 0:
            continue
        
        while check1 > 0:
            dx = x + 1
            dy = y - 1
            if 0 <= dx < n and 0 <= dy < n:
                x,y = dx,dy
                check1 -= 1
                tmp += graph[dx][dy]
            else:
                break
        if check1 != 0:
            continue

        while check2 > 0:
            dx = x + 1
            dy = y + 1
            if 0 <= dx < n and 0 <= dy < n:
                x,y = dx,dy
                tmp += graph[dx][dy]
                check2 -= 1
            else:
                break

        if check2 !=0:
            continue
      
        answer = max(answer,tmp)

print(answer)