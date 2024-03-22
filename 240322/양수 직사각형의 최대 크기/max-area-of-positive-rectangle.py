import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]


answer = 0
for i in range(n):
    for j in range(m):
        for k in range(i,n):
            for l in range(j,m):
                tmp = 0
                for a in range(i,k+1):
                    for b in range(j,l+1):
                        if graph[a][b] > 0:
                            tmp += 1
                        else:
                            tmp = 0
                            break
                answer = max(answer,tmp)

print(answer)