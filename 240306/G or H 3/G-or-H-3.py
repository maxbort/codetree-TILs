import sys

input = sys.stdin.readline

n,k = map(int,input().split())

alpha = ['O' for _ in range(100)]

for _ in range(n):
    a,b = map(str,input().split())
    alpha[int(a)] = b

answer = 0

for i in range(100-k):
    tmp = 0
    for j in range(k+1):
        if alpha[i+j] == 'H':
            tmp += 2
        if alpha[i+j] == 'G':
            tmp += 1
    answer = max(answer,tmp)

print(answer)