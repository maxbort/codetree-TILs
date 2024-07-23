n = int(input())

d = [0] * 100

for _ in range(n):
    idx, alpha = input().split()

    if alpha == 'H':
        d[int(idx)] = -1
    else:
        d[int(idx)] = 1

val = 0
for i in range(100):
    if d[i] != 0:
        for j in range(i,100):
            if d[j] != 0:
                cnt = sum(d[i:j+1])
        
                if cnt == 0:
                    val = max(val, abs(j-i))

print(val)