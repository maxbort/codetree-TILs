import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

num_set = []

for _ in range(n):
    x,y = map(int,input().split())

    num_set.append([y,x])
num_set.sort(key=lambda x : x[0])

num_set = deque(num_set)

max_sum = 0
while len(num_set) > 1:
    max_value, max_cnt = num_set.pop()
    min_value, min_cnt= num_set.popleft()
   

    if max_cnt > min_cnt:
        max_cnt -= min_cnt
        max_sum = max(max_sum, max_value + min_value)
        num_set.append((max_value,max_cnt))
        

    elif max_cnt == min_cnt:
        max_sum = max(max_sum, max_value + min_value)
    
    else:
        min_cnt -= max_cnt
        max_sum = max(max_sum, max_value + min_value)
        num_set.appendleft(min_value,min_cnt)


    # max_value = max(num_set.keys())
    # min_value = min(num_set.keys())
    # max_cnt = num_set.get(max_value)
    # min_cnt = num_set.get(min_value)

    # if max_cnt > min_cnt:
    #     max_cnt -= min_cnt
    #     max_sum = max(max_sum, max_value + min_value)
    #     num_set.pop(min_value,None)
    #     num_set[max_value] = max_cnt

    # elif max_cnt == min_cnt:
    #     num_set.pop(min_value,None)
    #     num_set.pop(max_value,None)
    #     max_sum = max(max_sum, max_value + min_value)
    
    # else:
    #     min_cnt -= max_cnt
    #     max_sum = max(max_sum, max_value + min_value)
    #     num_set.pop(max_value,None)
    #     num_set[min_value] = min_cnt

if num_set:
    last_value,last_cnt = num_set.pop()
    max_sum = max(max_sum,last_value * 2)

print(max_sum)