import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int,input().split()))

first = min(num_list)

second = float('inf')
answer = -1
check = 0
for idx,num in enumerate(num_list):
    if num == first:
        continue
    elif num > first:
        if num < second:
            check == 0
            second = num
            answer = idx+1
        elif num == check:
            check += 1
if check >= 1:
    print(-1)
else:
    print(answer)