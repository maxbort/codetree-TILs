import sys

input = sys.stdin.readline

n,m = map(int,input().split())

answer = 0
graph = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n-m+1):
        check = graph[i][j]
        cnt = 0
        for k in range(m):
            if check == graph[i][j+k]:
                cnt += 1
            else:
                break
        if cnt == m:
            answer += 1
            break

for i in range(n):
    for j in range(n-m+1):
        check = graph[j][i]
        cnt = 0
        for k in range(m):
            if check == graph[j+k][i]:
                cnt += 1
            else:
                break
        if cnt == m:
            answer += 1
            break

print(answer)