import sys

input = sys.stdin.readline

n,k = map(int,input().split())

num_list = list(map(int,input().split()))

answer = 0
for i in range(n-k+1):
    tmp = 0
    for j in range(k):
        tmp += num_list[i+j]
    answer = max(answer,tmp)
print(answer)