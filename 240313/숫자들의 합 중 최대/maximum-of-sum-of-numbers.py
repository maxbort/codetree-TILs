import sys

input = sys.stdin.readline

x, y = map(str,input().rstrip().split())

sum_x = 0
sum_y = 0
for i in x:
    sum_x += int(i)
for j in y:
    sum_y += int(j)

print(max(sum_x,sum_y))