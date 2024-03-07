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
        for k in range(n+1): # 채굴 범위 지정
            loss = cal_loss(k) # 손실 계산
            tmp = 0
            visit = [[False for _ in range(n)] for _ in range(n)]
            for dx in range(k+1): # 범위 내 금 개수 찾기
                dy = k-dx
                for ddx in range(dx+1):
                    for ddy in range(dy+1):
                        if 0 <= i + ddx < n and 0 <= j+ddy < n and not visit[i+ddx][j+ddy]:
                            tmp += graph[i+ddx][j + ddy]
                            visit[i+ddx][j+ddy] = True
                        if 0 <= i + ddx < n and 0 <= j-ddy < n and not visit[i+ddx][j-ddy]:
                            tmp += graph[i+ddx][j - ddy]
                            visit[i+ddx][j-ddy] = True
                        if 0 <= i - ddx < n and 0 <= j+ddy < n and not visit[i-ddx][j+ddy]:
                            tmp += graph[i-ddx][j + ddy]
                            visit[i-ddx][j+ddy] = True
                        if 0 <= i - ddx < n and 0 <= j-ddy < n and not visit[i-ddx][j-ddy]:
                            tmp += graph[i-ddx][j - ddy]
                            visit[i-ddx][j-ddy] = True
                
            if loss <= tmp*m:

                answer = max(answer,tmp)
print(answer)