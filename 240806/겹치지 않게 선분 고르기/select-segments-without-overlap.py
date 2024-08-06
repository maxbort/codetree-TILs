n = int(input())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

arr.sort()

d = [1] * n

for i in range(1,n):
    for j in range(i):
        x,y = arr[i]
        x2,y2 = arr[j]

        if y2 < x:
            d[i] = max(d[i], d[j] + 1)
print(max(d))