import sys

n,s = map(int,input().split())
arr = list(map(int,input().split()))

min_gap = sys.maxsize
total = sum(arr)

for i in range(n-1):
    for j in range(i+1,n):
        min_gap = min(min_gap ,abs(s -(total - arr[i] - arr[j])))

print(min_gap)