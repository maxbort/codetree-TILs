n = int(input())

arr = [
    tuple(input().split())
    for _ in range(n)
]

temp = [0 for _ in range(201)]

cur = 100

for length, direct in arr:
    
    if direct == 'R':
        for i in range(int(length)):
            temp[cur + i] += 1
        cur += int(length)

    if direct == 'L':
        for i in range(1,int(length)+1):
            temp[cur - i] += 1
        cur -= int(length)

cnt = 0
for i in temp:
    if i >= 2:
        cnt += 1
print(cnt)