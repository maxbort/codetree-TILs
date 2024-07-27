import sys
a,b = map(int,input().split())

max_val = -sys.maxsize
for i in range(a,b+1):
    cnt = 0
    for j in str(i):
        cnt += int(j)
    max_val = max(max_val, cnt)
print(max_val)