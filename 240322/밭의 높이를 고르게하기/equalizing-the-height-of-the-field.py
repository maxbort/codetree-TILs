import sys

input = sys.stdin.readline

n,h,t = map(int,input().split())

h_info = list(map(int,input().split()))

answer = float('inf')

h_info.sort(key=lambda x : abs(x-h))
tmp = 0
for j in range(t):
    tmp += abs(h-h_info[j])
answer = min(answer,tmp)

print(answer)