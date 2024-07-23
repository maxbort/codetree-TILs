import sys

n,h,t = map(int,input().split())
arr = list(map(int,input().split()))

gap = []

for i in arr:
    gap.append(abs(i-h))

min_cost = sys.maxsize

for i in range(n-t+1):
    min_cost = min(min_cost, sum(gap[i:i+t]))

print(min_cost)