import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

num = list(map(int,input().split()))

answer = float('inf')
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        q = deque()
        tmp = 0
        for k in range(n):
            if i == k:
                q.append(2*num[k])
            elif k == j:
                continue
            else:
                q.append(num[k])
        while q:
            if len(q) == 1:
                break
            a = q.popleft()
            b = q.popleft()
            tmp += abs(a-b)
            q.appendleft(b)
        answer = min(answer,tmp)        

print(answer)