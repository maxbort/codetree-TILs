import sys

t,a,b = map(int,input().split())

arr = [
    list(input().split())
    for _ in range(t)
]

visited = ['.' for _ in range(b+1)]

for alpha, idx in arr:
    visited[int(idx)] = alpha

cnt = 0

for i in range(a,b+1):
    min_dist_d1, min_dist_d2 = sys.maxsize, sys.maxsize

    for j in range(a,b+1):
        
        if visited[j] == 'S':
            min_dist_d1 = min(min_dist_d1, abs(i-j)+1)
            
        if visited[j] == 'N':
            min_dist_d2 = min(min_dist_d2, abs(i-j)+1)
        
    
    if min_dist_d1 <= min_dist_d2:
        cnt += 1
print(cnt)