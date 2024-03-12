import sys

input = sys.stdin.readline

x, y = map(int,input().split())

answer=  0

for i in range(x,y+1):
    cnt = 0
    standard = max(set(str(i)), key = str(i).count)
    for j in (str(i)):
        if j == standard:
            continue
        else:
            cnt += 1
        if cnt >= 2:
            break
    if cnt == 1:
        answer += 1

print(answer)