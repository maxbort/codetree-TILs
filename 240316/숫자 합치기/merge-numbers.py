import sys
from collections import deque

input = sys.stdin.readline
from collections import deque
n = int(input())

num = list(map(int,input().split()))

num.sort(reverse = True)
answer = 0
while len(num) > 2:
    tmp = []
    a = num.pop()
    b = num.pop()
    answer += a+b
    num.append(a+b)
    num.sort(reverse = True)

if len(num) == 2:
    answer += sum(num)

print(answer)