import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))

answer = 0
for i in range(1,50):
    for j in range(n-1):
        for k in range(j,n):
            large = max(num[j],num[k])
            small = min(num[j],num[k])
            if large - i == small + i:
                answer += 1

print(answer)