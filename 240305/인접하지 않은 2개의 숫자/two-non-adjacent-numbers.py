import sys

input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))

answer = 0
for i in range(n-2):
    first = num_list[i]
    for j in range(i+2,n):
        answer = max(answer,first+num_list[j])

print(answer)