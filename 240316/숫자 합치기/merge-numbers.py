import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())
 
num = list(map(int,input().split()))

num.sort()

answer=  0
tmp =[]
while True:
    tmp = []
    for i in range(0,len(num),2):
        if i < len(num):
            tmp.append(num[i] + num[i+1])
        else:
            tmp.append(num[i])
    answer += sum(tmp)
    num = deepcopy(tmp)
    if len(num) == 2:
        answer += sum(tmp)
        break

print(answer)