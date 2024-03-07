import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

def cal_loss(k):
    return k*k + (k+1)**2

# k 번움직여서 닿는 곳 -> 마름모 범위?
answer = 0
for i in range(n):
    for j in range(n):
        for a in range(n):
            loss = cal_loss(a)
            tmp = 0
            visit = [[False for _ in range(n)] for _ in range(n)]
            for b in range(a+1):
                plus_x = b
                plus_y = a-b
                if 0 <= i+plus_x < n and 0 <= j + plus_y < n and not visit[i+plus_x][j+plus_y]:
                    tmp += graph[i+plus_x][j+plus_y]
                    visit[i+plus_x][j+plus_y] = True
                if 0 <= i+plus_x < n and 0 <= j - plus_y < n and not visit[i+plus_x][j-plus_y]:
                    tmp += graph[i+plus_x][j-plus_y]
                    visit[i+plus_x][j-plus_y] = True
                if 0 <= i-plus_x < n and 0 <= j + plus_y < n and not visit[i-plus_x][j+plus_y]:
                    tmp += graph[i-plus_x][j+plus_y]
                    visit[i-plus_x][j+plus_y] = True
                if 0 <= i-plus_x < n and 0 <= j - plus_y < n and not visit[i-plus_x][j-plus_y]:
                    tmp += graph[i-plus_x][j-plus_y]
                    visit[i-plus_x][j-plus_y] = True

            if m*tmp >= loss:
                answer = max(answer, tmp)

print(answer)