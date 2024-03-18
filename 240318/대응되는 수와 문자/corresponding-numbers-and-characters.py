import sys

input = sys.stdin.readline

n, m = map(int,input().split())

di = {}

for i in range(n):
    a = str(input().rstrip())
    di[a] = i+1

for _ in range(m):
    a = input().rstrip()
    if a.isdigit():
        for k,v in di.items():
            if v == int(a):
                print(k)
            
    else:
        print(di.get(a))