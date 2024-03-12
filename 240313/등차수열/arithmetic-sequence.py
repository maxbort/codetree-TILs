import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))

answer = 0
for dk in range(1,50):
    tmp = 0

    for j in range(n-1):
        for k in range(j+1,n):
            if num[j] - dk == dk - num[k]:
                tmp += 1
    answer = max(tmp,answer)

print(answer)