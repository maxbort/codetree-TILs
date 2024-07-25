import sys

n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]


min_val = sys.maxsize
for i in range(n):
    for j in range(n):

        if i == j:
            continue
        
        x1,y1 = arr[i]
        x2,y2 = arr[j]

        min_val = min(min_val, (x2-x1) ** 2 + (y2-y1) ** 2)
print(min_val)