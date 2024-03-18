import sys

input = sys.stdin.readline

n,k = map(int,input().split())
num_list = list(map(int,input().split()))
answer = 0
cnt = {}

for num in num_list:
    if num in cnt:
        cnt[num] += 1
    else:
        cnt[num] = 1

for i in range(n):
    cnt[num_list[i]] -= 1

    for j in range(i):
        diff = k - num_list[i] - num_list[j]

        if diff in cnt:
            answer += cnt[diff]
print(answer)