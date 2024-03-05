import sys

input = sys.stdin.readline

n = int(input())

point = []
for _ in range(n):
    point.append(list(map(int,input().split())))


dist = float('inf')

for i in range(1,n-1):
    tmp = 0
    for j in range(0,i-1):
        tmp += abs(point[j][0] - point[j+1][0]) + abs(point[j][1] - point[j+1][1])
    tmp += abs(point[i-1][0] - point[i+1][0]) + abs(point[i-1][1] - point[i+1][1])
    for k in range(i+1,n-1):
        tmp += abs(point[k][0] - point[k+1][0]) + abs(point[k][1] - point[k+1][1])
    
    dist = min(dist,tmp)
print(dist)