n = int(input())

arr = [
    tuple(input().split())
    for _ in range(n)
]

# L, R , last
white = [0] * 200001
black = [0] * 200001
color = [0] * 200001

cur = 100000

for l, d in arr:
    l = int(l)

    if d == 'L':
        for i in range(cur-l+1, cur+1):
            color[i] = 1
            white[i] += 1
        cur -= l-1
    else:
        for i in range(cur, cur+l):
            color[i] = 2
            black[i] += 1
        cur += l-1

w,b,g = 0,0,0
for i in range(len(color)):
    if white[i] >= 2 and black[i] >= 2:
        g += 1
    elif color[i] == 1:
        w += 1
    elif color[i] == 2:
        b += 1
print(w,b,g)