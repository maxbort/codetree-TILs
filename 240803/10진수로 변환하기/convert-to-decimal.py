n = list(map(int,input()))

n.reverse()

cnt = 0
for i in range(len(n)):
    if n[i] == 1:
        cnt += 2 ** i
print(cnt)