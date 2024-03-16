import sys
from functools import cmp_to_key

input = sys.stdin.readline

n = int(input())
 
num = [str(input().rstrip()) for _ in range(n)]

def compare(a,b):
    if str(a) + str(b) > str(b) + str(a):
        return -1
    
    if str(a) + str(b) > str(b) + str(a):
        return 1

    return 0

num.sort(key=cmp_to_key(compare))

for i in num:
    print(i,end="")