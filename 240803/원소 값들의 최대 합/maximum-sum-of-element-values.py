from collections import deque

n,m = map(int,input().split())
arr = list(map(int,input().split()))


q = deque(sorted(arr, reverse=True))

idx, cnt = 0,0
while q:
    data = q.popleft()

    cnt += data
    idx += 1

    if idx == m:
        break
print(cnt)