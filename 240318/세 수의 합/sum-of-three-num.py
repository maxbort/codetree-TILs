import sys

input = sys.stdin.readline

n,k = map(int,input().split())

num_list = list(map(int,input().split()))
answer = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for l in range(j+1,n):
            if num_list[i] + num_list[j] + num_list[l] == k:
                answer += 1

print(answer)