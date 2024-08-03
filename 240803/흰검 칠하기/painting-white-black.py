n = int(input())

arr = [
    tuple(input().split())
    for _ in range(n)
]

# L, R , last
temp = [[0,0,0] for _ in range(200001)]

cur = 100000

for l, d in arr:
    l = int(l)

    if d == 'R':
        for i in range(l):
            if temp[cur+i][2] == 3:
                continue
            temp[cur+i][1] += 1
            temp[cur+i][2] = 2
            if temp[cur+i][0] >= 2 and temp[cur+i][1] >= 2:
                temp[cur+i][2] = 3

        cur += l

    if d == 'L':
        for i in range(1,l+1):
            if temp[cur-i][2] == 3:
                continue
            temp[cur-i][0] += 1
            temp[cur-i][2] = 1
            if temp[cur-i][0] >= 2 and temp[cur-i][1] >= 2:
                temp[cur-i][2] = 3
        cur -= l

one_c,two_c,third_c = 0,0,0

for _,_,last in temp:
    if last == 1:
        one_c += 1
    elif last == 2:
        two_c += 1
    elif last == 3:
        third_c += 1

print(one_c, two_c, third_c)