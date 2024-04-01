import sys
from itertools import combinations

input = sys.stdin.readline

n,m = map(int,input().split())

n_list = list(map(int,input().split()))

answer = 0

choose_num = list(combinations(n_list,m))

for candi in choose_num:
    tmp = 0
    for k in candi:
        if tmp == 0:
            tmp = k
        else:
            tmp = tmp ^ k
    answer = max(tmp,answer)
print(answer)

### 백트래킹 방식

# answer = 0
# def find_max(curr_idx, cnt, curr_val):
#     global answer

#     if cnt == m:
#         answer = max(answer,curr_val)
#         return
#     if curr_ix == n:
#         return

#     # curr_idx 숫자 선택 x
#     find_max(curr_idx+1, cnt, curr_val)

#     # curr_idx 숫자 선택 o
#     find_max(curr_idx+1, cnt+1, curr_idx ^ n_list[curr_idx])

# find_max(0,0,0)
# print(answer)