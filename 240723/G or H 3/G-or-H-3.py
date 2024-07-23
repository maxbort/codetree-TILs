n,k = map(int,input().split())

d = [0] * 10000

for _ in range(n):
    idx, alpha = input().split()

    if alpha == 'H':
        d[int(idx)] = 2
    else:
        d[int(idx)] = 1

max_val = 0
for i in range(10001 - k):
    max_val = max(max_val,sum(d[i:i+k+1]))

print(max_val)