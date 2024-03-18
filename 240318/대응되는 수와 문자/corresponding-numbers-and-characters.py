import sys

input = sys.stdin.readline

n, m = map(int,input().split())

di = {}
di_num = {}
for i in range(n):
    a = str(input().rstrip())
    di[a] = i+1
    di_num[i+1] = a
for _ in range(m):
    a = input().rstrip()
    if a.isdigit():
        print(di_num.get(int(a)))
    else:
        print(di.get(a))