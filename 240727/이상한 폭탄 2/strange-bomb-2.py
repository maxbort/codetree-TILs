n,k = map(int,input().split())

arr = [
    int(input())
    for _ in range(n)
]

ans = -1

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        
        if arr[i] == arr[j]:
            if k >= abs(j-i):
                ans = max(ans, arr[i])
print(ans)