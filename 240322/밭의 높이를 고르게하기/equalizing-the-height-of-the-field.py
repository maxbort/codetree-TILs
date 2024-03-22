import sys

input = sys.stdin.readline

n,h,t = map(int,input().split())

h_info = list(map(int,input().split()))

answer = float('inf')
for i in range(n-t+1):
    tmp = 0
    for j in range(i,i+t):
        tmp += abs(h-h_info[j])
    answer = min(answer,tmp)
print(answer)