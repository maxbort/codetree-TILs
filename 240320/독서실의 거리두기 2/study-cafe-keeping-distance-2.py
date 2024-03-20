import sys

input = sys.stdin.readline

n = int(input())


seat = list(input().rstrip())

dist = []
tmp = [0,1,0]
for i in range(1,n):
    if i == n-1:
        tmp[-1] = i
        dist.append(tmp)
    if seat[i] == '1':
        tmp[-1] = i
        dist.append(tmp)
        tmp = [i,1,0]
    else:
        tmp[1]+= 1

first_p = 0
last_p = 0
for i in range(n):
    if seat[i] == '1':
        first_p = i
        break
for i in range(n-1,0,-1):
    if seat[i] == '1':
        last_p = i
        break


a= max(dist,key= lambda x : x[1])
b = min(dist,key=lambda x : x[1])
answer = b[1]

new_one = (a[0]+a[2])//2

if seat[0] == '0':
    answer = min(answer,new_one-a[0],a[2]-new_one)
    answer = max(answer,first_p)
elif seat[-1] == '0':
    answer = min(answer,new_one-a[0],a[2]-new_one)
    answer = max(answer,n-last_p-1)
else:
    answer = min(answer,new_one-a[0],a[2]-new_one)
print(answer)