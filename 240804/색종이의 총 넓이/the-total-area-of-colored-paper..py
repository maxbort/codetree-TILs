OFFSET = 100

n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

temp = [
    [0 for _ in range(201)]
    for _ in range(201)
]

for x,y in arr:
    x += OFFSET
    y += OFFSET

    for i in range(x,x+8):
        for j in range(y,y+8):
            temp[i][j] = 1

print(sum(sum(row) for row in temp))