import sys

input = sys.stdin.readline

n = int(input())

point_list = [list(map(int,input().split())) for _ in range(n)]

answer = float('inf')

for i in range(0,101,2):
    for j in range(0,101,2):
        tmp1 = 0
        tmp2 = 0
        tmp3 = 0
        tmp4 = 0
        for x,y in point_list:
            if x > i and y > j:
                tmp1 += 1
            if x > i and y < j:
                tmp2 += 1
            if x < i and y > j:
                tmp3 += 1
            if x < i and y < j:
                tmp4 += 1
        tmp = max(tmp1,tmp2,tmp3,tmp4)
        answer = min(tmp,answer)

print(answer)