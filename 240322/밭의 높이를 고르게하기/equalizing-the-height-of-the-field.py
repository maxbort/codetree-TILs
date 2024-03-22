import sys

input = sys.stdin.readline

n,h,t = map(int,input().split())

h_info = list(map(int,input().split()))

answer = float('inf')

for i in range(n):
    check =h_info[i]
    h_info.sort(key=lambda x : (x-check))
    tmp = 0
    for j in range(t):
        tmp += abs(check-h_info[j])
    answer = min(answer,tmp)

print(answer)