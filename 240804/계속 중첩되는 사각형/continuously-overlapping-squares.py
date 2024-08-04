n = int(input())

OFFSET = 100

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

temp = [
    [0 for _ in range(201)]
    for _ in range(201)
]

for i, (x1,y1,x2,y2) in enumerate(arr, start = 1):
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    if i % 2 == 1:
        for x in range(x1,x2):
            for y in range(y1,y2):
                temp[x][y] = 0
    else:
        for x in range(x1,x2):
            for y in range(y1,y2):
                temp[x][y] = 1

print(sum(sum(row) for row in temp))