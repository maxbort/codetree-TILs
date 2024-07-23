from itertools import permutations as pm

n,m = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

b_pm = list(pm(b,len(b)))

cnt = 0
for i in range(n-len(b)+1):
    for j in b_pm:
        flag = True
        for k in range(len(b)):
            if j[k] != a[i:i+len(b)][k]:
                flag = False
                break

        if flag:
            cnt += 1
            break

print(cnt)