import sys
from itertools import product

input = sys.stdin.readline

k,n = map(int,input().split())

num_list = []

for i in range(k):
    num_list.append(i+1)

answer = list(product(num_list,repeat=n))

for i,j in answer:
    print(i,j)