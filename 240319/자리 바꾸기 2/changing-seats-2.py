import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int,input().split())

seat_list = [list(map(int,input().split())) for _ in range(k)]

people = [[] for _ in range(n)]
answer = [[] for _ in range(n)]
for i in range(n):
    people[i].append(i+1)
    answer[i].append(i+1)

for _ in range(3):
    for a,b in seat_list:
        x,y = people[a-1][-1],people[b-1][-1]
        
        people[a-1].append(y)
        people[b-1].append(x)
        answer[x-1].append(b)
        answer[y-1].append(a)
        
        
for i in answer:
    print(len(set(i)))