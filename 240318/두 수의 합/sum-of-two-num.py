import sys

input = sys.stdin.readline

n,k = map(int,input().split())

num_list = list(map(int,input().split()))

sum_dict = {}

for i in num_list:
    if i not in sum_dict:
        sum_dict[i] = 1
    else:
        sum_dict[i] += 1

answer = 0
for key,value in sum_dict.items():
    a = k - key
    if a in sum_dict:
        answer += min(value,sum_dict[a])
        sum_dict[a] = 0
print(answer)