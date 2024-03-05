import sys

input = sys.stdin.readline

n = int(input())

room = []
for _ in range(n):
    room.append(int(input()))

dist = float('inf')

for i in range(n):
    final_dist = 0
    for j in range(n):
        if i <= j:
            move_dist = j-i
        else:
            move_dist = n-i+j

        final_dist += room[j] * move_dist
    
    dist = min(dist,final_dist)

print(dist)