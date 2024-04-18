import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int,input().split()))

num_list.sort()
answer = float('inf')

for i in range(n):
    answer = min(answer,num_list[n+i] - num_list[i])
print(answer)