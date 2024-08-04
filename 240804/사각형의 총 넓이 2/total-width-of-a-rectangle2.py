n = int(input())

OFFSET = 100

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

temp = [
    [0 for _ in range(200)]
    for _ in range(200)
]

for x1,y1, x2,y2 in arr:
    for x in range(x1+OFFSET, x2+OFFSET):
        for y in range(y1+OFFSET, y2+OFFSET):
            temp[x][y] = 1

print(sum(sum(row) for row in temp))