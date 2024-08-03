import heapq

n,m = map(int,input().split())
arr = list(map(int,input().split()))


def heapsort(arr):
	h = []
	res = []
	for v in arr:
		heapq.heappush(h,-v) #차례로 삽입
	for i in range(len(h)):
		res.append(-heapq.heappop(h))
	return res

cnt = 0
for i in range(m):
    cnt += heapsort(arr)[i]

print(cnt)