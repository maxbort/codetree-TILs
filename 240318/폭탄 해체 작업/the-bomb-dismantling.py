import sys

input = sys.stdin.readline

n = int(input())
time_limit = 0
bomb_list = []

for _ in range(n):
    a,b = map(int,input().split())
    bomb_list.append([a,b])

bomb_list.sort(key = lambda x : (-x[0],x[1]))
answer = 0

for i in bomb_list:
    if time_limit > i[1]:
        break
    answer += i[0]
    time_limit += 1
    
print(answer)