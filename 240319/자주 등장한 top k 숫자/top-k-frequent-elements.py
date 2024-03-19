import heapq

di = {}

n,k = map(int,input().split())

num_list = list(map(int,input().split()))

for a in num_list:
    if a in di:
        di[a] += 1
    else:
        di[a] = 1

sorted_di = sorted(di.items(), key=lambda x : (-x[1], -x[0]))

m = 1
for k,v in sorted_di:
    print(k,end=' ')
    m += 1
    if m > k:
        break