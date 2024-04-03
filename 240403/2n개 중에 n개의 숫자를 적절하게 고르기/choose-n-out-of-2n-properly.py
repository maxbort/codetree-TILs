import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

num_list = list(map(int,input().split()))


answer = float('inf')

idx_list = [i for i in range(2*n)]

candi = list(combinations(idx_list,n))

for i in candi:
    a_sum = 0
    b_sum = 0
    for j in range(2*n):
        if j in i:
            b_sum += num_list[j]
        else:
            a_sum += num_list[j]

    answer = min(answer,abs(a_sum - b_sum))
print(answer)