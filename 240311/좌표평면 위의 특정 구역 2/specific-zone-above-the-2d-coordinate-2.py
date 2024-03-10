import sys
from collections import deque
iuput = sys.stdin.readline

n = int(input())

line = []
for _ in range(n):
    line.append(list(map(int,input().split())))

answer = float('inf')
for i in range(n):
    q = deque()
    large_x = -float('inf')
    large_y = -float('inf')
    small_x = float('inf')
    small_y = float('inf')

    for j in range(0,i):
        q.append(line[j])
    for k in range(i+1,n):
        q.append(line[k])
    while q:
        x,y = q.pop()
        large_x = max(large_x,x)
        large_y = max(large_y,y)
        small_x = min(small_x,x)
        small_y = min(small_y,y)

    
    answer = min(answer,(abs(large_x-small_x) * abs(large_y-small_y)))

print(answer)