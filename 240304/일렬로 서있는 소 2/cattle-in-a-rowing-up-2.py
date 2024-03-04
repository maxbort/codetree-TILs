import sys

input = sys.stdin.readline

n = int(input())
cow = list(map(int,input().split()))

answer = 0

for i in range(n):
    point = cow[i]
    for j in range(i+1,n):
        if cow[i] <= cow[j]:
            point2 = cow[j]
            for k in range(j+1,n):
                if cow[j] <= cow[k]:
                    answer+=1

print(answer)