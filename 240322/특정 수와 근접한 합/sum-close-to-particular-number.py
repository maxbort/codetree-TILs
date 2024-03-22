import sys

input = sys.stdin.readline

n,s = map(int,input().split())

num_list = list(map(int,input().split()))

answer = float('inf')
for i in range(n-1):
    for j in range(i+1,n):
        a = sum(num_list[:i])
        b = sum(num_list[i+1:j])
        c = sum(num_list[j+1:])
        answer = min(answer,abs(s-a-b-c))
print(answer)