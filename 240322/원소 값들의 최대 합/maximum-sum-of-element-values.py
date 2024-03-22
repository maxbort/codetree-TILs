import sys

input = sys.stdin.readline

n, m = map(int,input().split())

num_list = list(map(int,input().split()))

answer = 0
for i in num_list:
    tmp = 0
    move = i-1
    for _ in range(m):
        tmp += num_list[move] 
        move = num_list[move] -1
    answer = max(answer,tmp)

print(answer)