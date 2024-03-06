import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int,input().split()))

answer = n
for i in range(n+1):
    if i == 1 or i == 0:
        continue
    else:
        for k in range(n-i+1):
            if sum(num_list[k:k+i])/i in num_list[k:k+i]:
                answer += 1
print(answer)