import sys

input = sys.stdin.readline

n = int(input())

iceberg = list(int(input()) for _ in range(n))

answer = 0
for h in range(max(iceberg)+1):
    tmp = 0
    flag = False
    for i in range(n):
        if iceberg[i] > h:
            if not flag:
                tmp += 1
                flag = True
        else:
            flag = False                

    answer = max(answer,tmp)
print(answer)