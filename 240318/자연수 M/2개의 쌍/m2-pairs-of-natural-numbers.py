import sys

input = sys.stdin.readline

n = int(input())

num_set = {}

for _ in range(n):
    x,y = map(int,input().split())

    num_set[y] = x

max_sum = 0
answer = float('inf')
while num_set:
    max_value = max(num_set.keys())
    min_value = min(num_set.keys())
    max_cnt = num_set.get(max_value)
    min_cnt = num_set.get(min_value)

    if max_cnt > min_cnt:
        max_cnt -= min_cnt
        max_sum = max(max_sum, max_value + min_value)
        num_set.pop(min_value,None)
        num_set[max_value] = max_cnt

    elif max_cnt == min_cnt:
        num_set.pop(min_value,None)
        num_set.pop(max_value,None)
        max_sum = max(max_sum, max_value + min_value)
    
    else:
        min_cnt -= max_cnt
        max_sum = max(max_sum, max_value + min_value)
        num_set.pop(max_value,None)
        num_set[min_value] = min_cnt

    answer = min(answer,max_sum)
print(answer)