import sys
from functools import cmp_to_key

input = sys.stdin.readline

def compare(x,y):
    if x > y:
        return -1
    if y > x:
        return 1
    return 0

n = int(input())

num = [int(input()) for _ in range(n)]

num.sort(key=cmp_to_key(compare))
num.sort(key=lambda x : len(str(x)))
for i in num:
    print(i,end='')