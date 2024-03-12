import sys

input = sys.stdin.readline

x, y = map(str,input().rstrip().split())

answer = 0
for i in range(int(x),int(y)+1):
    tmp = 0
    for j in str(i):
        tmp += int(j)
    answer = max(answer,tmp)
print(answer)