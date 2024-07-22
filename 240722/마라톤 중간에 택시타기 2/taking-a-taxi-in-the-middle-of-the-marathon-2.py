import sys
n = int(input())

arr = [
    list(map(int,input().split()))
    for i in range(n)
]

def get_dist(a,b):
    x1,y1 = a
    x2,y2 = b
    return abs(x1-x2) + abs(y1-y2)

min_dist = sys.maxsize

total_dist = 0
for i in range(n-1):
    total_dist += get_dist(arr[i], arr[i+1])

for i in range(1,n-1):
    dist = total_dist

    dist -= get_dist(arr[i], arr[i+1])
    dist -= get_dist(arr[i-1], arr[i])
    dist += get_dist(arr[i-1], arr[i+1])

    min_dist = min(min_dist, dist)

print(min_dist)