import sys

input = sys.stdin.readline

n = int(input())
home = list(map(int,input().split()))

answer = float('inf')

for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += abs(i-j) * (home[j])
        
    answer = min(answer,tmp)

print(answer)