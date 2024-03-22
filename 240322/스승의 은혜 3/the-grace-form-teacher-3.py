import sys

input = sys.stdin.readline

n,b = map(int,input().split())

price = [list(map(int,input().split())) for _ in range(n)]

answer = 0

for i in range(n):
    tmp = []
    for j in range(n):
        tot = 0
        if i == j:
            tot += price[j][0] //2 + price[j][1]
        else:
            tot += price[j][0] + price[j][1]
        tmp.append(tot)
    tmp.sort()

    can_s = 0
    bud = 0
    tmp_s = 0
    for a in tmp:
        bud += a
        if bud <= b:
            tmp_s += 1
        else:
            break

    answer = max(answer,tmp_s)
        
print(answer)