import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int,input().split()))

answer = 0
a = 0
while True:
    tmp = 0
    if num_list[a] <= 0:
        a += 1
    else:
        for i in range(a,n):
            tmp += num_list[i]
            answer = max(answer,tmp)
            if tmp < 0:
                a = i
                break
        if i == n-1:
            break
    
print(answer)