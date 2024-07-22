import sys
n = int(input())

# dist = [
#     map(int,input().split())
#     for i in range(n)
# ]
arr = []
for _ in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))

def get_dist(a,b):
    x1,y1 = a
    x2,y2 = b
    return abs(x1-x2) + abs(y1-y2)


point = 1
min_dist = sys.maxsize
total_dist = 0
for i in range(n-1):
    total_dist += get_dist(arr[i], arr[i+1])

#print(min_dist)

for i in range(1,n-1):
    dist = total_dist
    # print("before  total_dist : {}".format(total_dist))

    dist -= get_dist(arr[i], arr[i+1])
    dist -= get_dist(arr[i-1], arr[i])
    # print("minus dist : {}".format(dist))
    dist += get_dist(arr[i-1], arr[i+1])
    # print("plus dist : {}".format(dist))

    min_dist = min(min_dist, dist)
    # print("min_dist : {}".format(min_dist))

print(min_dist)