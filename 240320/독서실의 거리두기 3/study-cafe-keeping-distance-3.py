import sys

input = sys.stdin.readline

n = int(input())

seat = list(input().rstrip())

dist = []
tmp = [0,0,0]
for i in range(1,n):
    if seat[i] == '1':
        tmp[-1] = i
        dist.append(tmp)
        tmp = [i,0,0]
    else:
        tmp[1]+= 1

a= max(dist,key= lambda x : x[1])
b = min(dist,key=lambda x : x[1])
print(b)