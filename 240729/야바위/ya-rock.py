n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_val = 0
for i in range(1,4):
    visited = [False] * 4
    visited[i] = True

    cnt = 0

    for a,b,c in arr:
        visited[a], visited[b] = visited[b], visited[a]
        if visited[c]:
            cnt += 1
    
    max_val = max(max_val ,cnt)
print(max_val)