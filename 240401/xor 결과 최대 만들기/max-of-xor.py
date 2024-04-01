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