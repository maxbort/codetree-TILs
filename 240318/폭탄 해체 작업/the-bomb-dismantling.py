import sys
import heapq

MAX_TIME = 10000
input = sys.stdin.readline

n = int(input())
bomb_list = [list(map(int,input().split())) for _ in range(n)]

bomb_list.sort(key = lambda x : x[1])
pq = []
bomb_idx = n-1
answer = 0

for i in range(MAX_TIME, 0,-1):
    while bomb_idx >= 0 and bomb_list[bomb_idx][1] >= i:
        heapq.heappush(pq, -bomb_list[bomb_idx][0])
        bomb_idx -= 1
    
    if pq:
        answer += -heapq.heappop(pq)
print(answer)