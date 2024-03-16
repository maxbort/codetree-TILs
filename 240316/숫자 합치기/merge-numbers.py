import heapq

n = int(input())
num = list(map(int,input().split()))

pq = []
answer = 0

for i in num:
    heapq.heappush(pq,i)

while len(pq) > 1:
    x1 = heappop(pq)
    x2 = heappop(pq)

    answer += x1+x2
    heapq.heappush(pq,x1+x2)
print(answer)