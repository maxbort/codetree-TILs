import sys

input = sys.stdin.readline

n = int(input())
b_card = [int(input()) for _ in range(n)]

a_card = [i for i in range(2*n + 1)]

answer = 0
for i in b_card:
    a_card[i] = 0

for i in b_card:
    for j in range(i+1,len(a_card)):
        if a_card[j] != 0:
            a_card[j] = 0
            answer += 1
            break

print(answer)