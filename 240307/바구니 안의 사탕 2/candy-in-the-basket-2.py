import sys

input = sys.stdin.readline

n,k = map(int,input().split())

bag = [0 for _ in range(101)]
for _ in range(n):
    candy, point = map(int,input().split())
    bag[point] += candy

answer = 0
for i in range(k,101-k):
    tmp = sum(bag[i-k:i+k+1])
    answer = max(answer,tmp)
print(answer)