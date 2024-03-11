import sys

input = sys.stdin.readline

n,k = map(int,input().split())

bomb = [int(input()) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(i+1,n):
        if bomb[i] == bomb[j]:
            if j-i <=k:
                answer= max(answer,bomb[i])

print(answer)