import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

num = list(map(int,input().split()))

num.sort(reverse = True)

answer = 0
while len(num) > 1:
    tmp = []
    a = num.pop()
    b = num.pop()
    answer += a+b
    num.append(a+b)
    num.sort(reverse = True)


print(answer)