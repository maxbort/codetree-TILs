n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

tmp = [ 0 for _ in range(201)]

for x,y in arr:
    x += 100
    y += 100
    for i in range(x+1,y):
        tmp[i] += 1
print(max(tmp))