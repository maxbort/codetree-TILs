import sys
n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

min_val = sys.maxsize
for i in range(n):
    max_x,max_y = 0,0
    min_x,min_y = 40000, 40000
    
    for j in range(n):

        if i == j:
            continue

        x,y= arr[j]

        max_x = max(max_x, x)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        min_y = min(min_y, y)

    min_val = min(min_val, abs(max_x - min_x) * abs(max_y - min_y))

print(min_val)