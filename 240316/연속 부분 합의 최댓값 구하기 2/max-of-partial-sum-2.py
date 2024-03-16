import sys

input = sys.stdin.readline

n = int(input())

num = list(map(int,input().split()))

a = 0
answer = -float('inf')

while True:
    tmp = 0
    if a >= n-1:
        break
    else:
        a += 1
    for i in range(a,n):
        tmp += num[i]
        answer = max(answer,tmp)
        if tmp < 0:
            a = i
            break
print(answer)