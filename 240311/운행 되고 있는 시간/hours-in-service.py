import sys

input = sys.stdin.readline

n = int(input())
work_time = [list(map(int,input().split())) for _ in range(n)]

answer = 0

for i in range(n):
    time = [0 for _ in range(1001)]
    for j in range(0,i):
        start,end = work_time[j]
        for a in range(start,end):
            time[a]= 1
    for k in range(i+1,n):
        start,end = work_time[k]
        for a in range(start,end):
            time[a] = 1
    answer = max(answer,sum(time))

print(answer)