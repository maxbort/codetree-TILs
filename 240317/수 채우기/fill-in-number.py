import sys

input = sys.stdin.readline

n = int(input())

coin = [5,2]

answer = -1
tmp = 0
for i in coin:
    a = n//i
    n -= i * a
    tmp += a
    
if n == 0:
    print(tmp)
else:
    print(answer)