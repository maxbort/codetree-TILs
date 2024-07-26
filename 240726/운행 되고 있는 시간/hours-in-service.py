n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_cnt = 0
for i in range(n):
    visited = [0 for _ in range(1001)]

    for j in range(n):
        if i == j:
            continue
        
        x,y = arr[j]

        for k in range(x,y):
            visited[k] += 1
    
    cnt = 0
    for j in range(1001):
        if visited[j] == 1:
            cnt += 1
    
    max_cnt = max(max_cnt, cnt)
print(max_cnt)