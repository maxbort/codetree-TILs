n,m,k = map(int,input().split())

arr = [
    int(input())
    for _ in range(m)
]

temp = [0 for _ in range(n+1)]

ans = -1
for i in arr:
    temp[i] += 1
    if temp[i] >= k:
        ans = i
        break
print(ans)