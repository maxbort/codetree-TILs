import sys

input = sys.stdin.readline

n,m,c = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]



def calValue(x, y, tmp, cnt):
    # 종료 조건이 되었을 때 현재 tmp에 대한 가치 계산 후 반환
    if cnt == m-1:
        value = sum(i*i for i in tmp)
        return value

    # tmp의 합이 c를 초과하면 마지막 값을 제거하고 계산
    if sum(tmp) > c:
        tmp.pop()
        return sum(i*i for i in tmp) if tmp else 0

    value = 0
    if y+cnt < len(graph[x]):
        # 현재 위치의 값을 추가하는 경우
        tmp.append(graph[x][y+cnt])
        value_with = calValue(x, y, tmp, cnt+1)
        tmp.pop()

        # 현재 위치의 값을 추가하지 않는 경우
        value_without = calValue(x, y, tmp, cnt+1)

        # 두 경우 중 최댓값 선택
        value = max(value_with if value_with is not None else 0, 
                    value_without if value_without is not None else 0)

    return value



answer = 0
for i in range(n):
    for j in range(n-m+1):
        for k in range(n):
            for l in range(n-m+1):
                a = []
                q,w = 0,0
                if i == k:
                    if j <= n-2*m:
                        l = j+m
                        q = calValue(i,j,a,0)
                        w = calValue(k,l,a,0)
                        answer = max(answer,calValue(i,j,a,0) + calValue(k,l,a,0))

                else:
                    q = calValue(i,j,a,0)
                    w = calValue(k,l,a,0)
                    answer = max(answer,calValue(i,j,a,0) + calValue(k,l,a,0))



print(answer)