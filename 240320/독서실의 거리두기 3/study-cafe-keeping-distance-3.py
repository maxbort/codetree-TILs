import sys

input = sys.stdin.readline

n = int(input())

seat = list(input().rstrip())

dist = []
tmp = [0,1,0]
for i in range(1,n):
    if seat[i] == '1':
        tmp[-1] = i
        dist.append(tmp)
        tmp = [i,1,0]
    else:
        tmp[1]+= 1

a= max(dist,key= lambda x : x[1])
b = min(dist,key=lambda x : x[1])
answer = b[1]
for i in range(a[0]+2, (a[0]+a[2])//2+1):
    if  i-a[0] <= answer and a[2]-i <= answer:
        answer = i-a[0]
if seat.count('0') < 3:
    print(1)
else:   
    print(answer)