import sys

input = sys.stdin.readline

t,a,b = map(int,input().split())

line = ['O' for _ in range(1001)]

for _ in range(t):
    c,d = map(str,input().split())

    line[int(d)] = c

answer = 0
for i in range(a,b+1):
    d1 = b+1
    d2 = b+1
    for j in range(a,b+1):
        if line[j] == 'S':
            d1 = min(d1,abs(j-i))
        if line[j] == 'N':
            d2 = min(d2,abs(j-i))

    if d2 >= d1:
        answer += 1
    
print(answer)