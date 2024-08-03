n,k = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(k)
]

tmp = [0 for _ in range(n+1)]

for a, b in arr:
    for i in range(a,b+1):
        tmp[i] += 1
print(max(tmp))