OFFSET = 1000

a_x1, a_y1, a_x2, a_y2 = map(int,input().split())
b_x1, b_y1, b_x2, b_y2 = map(int,input().split())

temp = [
    [0 for _ in range(2001)]
    for _ in range(2001)
]

for x in range(a_x1+OFFSET, a_x2+OFFSET):
    for y in range(a_y1+OFFSET, a_y2+OFFSET):
        temp[x][y] = 1

for x in range(b_x1+OFFSET, b_x2+OFFSET):
    for y in range(b_y1+OFFSET, b_y2+OFFSET):
        temp[x][y] = 0

min_x, min_y, max_x, max_y = 2001,2001,0,0

for i in range(2001):
    for j in range(2001):
        if temp[i][j] == 1:
            min_x = min(min_x,i)
            min_y = min(min_y,j)
            max_x = max(max_x,i)
            max_y = max(max_y,j)

if (min_x,min_y,max_x,max_y) != (2001,2001,0,0):
    print((max_x-min_x+1) * (max_y-min_y+1))
else:
    print(0)