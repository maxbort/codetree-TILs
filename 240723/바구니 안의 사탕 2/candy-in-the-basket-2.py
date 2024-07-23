n,k = map(int,input().split())

d = [0] * 101

for _ in range(n):
    a,b = map(int,input().split())
    d[b] = a

max_val = 0
for i in range(k, 101-k):
    max_val = max(max_val, sum(d[i-k:i+k+1]))
print(max_val)