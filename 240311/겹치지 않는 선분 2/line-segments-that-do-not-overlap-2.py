import sys

input = sys.stdin.readline

n = int(input())

line_list = [list(map(int,input().split())) for _ in range(n)]

line_list.sort(key=lambda x : (x[0],x[1]))
answer = 0
for i in range(n):
    flag = True
    for j in range(n):
        if i == j:
            continue
        else:
            x1,x2 = line_list[i]
            x3,x4 = line_list[j]

            if x1 < x3 and x4 < x2:
                flag =False
                break
            if x3 < x1 and x2 < x4:
                flag = False
                break
    if flag:
        answer += 1
print(answer)