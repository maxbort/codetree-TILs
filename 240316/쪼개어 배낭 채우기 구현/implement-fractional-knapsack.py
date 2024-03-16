import sys

input = sys.stdin.readline

n,m = map(int,input().split())

jew = []

for _ in range(n):
    a,b = map(int,input().split())
    jew.append([b,b/a,a])

jew.sort(key = lambda x : x[1], reverse=True)

answer= 0
for rv,v,w in jew:
    if w < m:
        answer += rv
        m -= w
    else:
        for _ in range(w):
            answer += v
            m-=1
            if m == 0:
                break
        if m == 0:
            break
print("{:.3f}".format(round(answer,3)))