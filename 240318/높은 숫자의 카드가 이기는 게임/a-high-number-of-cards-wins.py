import sys

input = sys.stdin.readline

n = int(input())
b_card = [int(input()) for _ in range(n)]
b_set = set(b_card)
a_card = []
answer = 0
for i in range(1,2*n+1):
    if i not in b_set:
        a_card.append(i)

answer = 0
b_idx = 0
a_card.sort()
b_card.sort()
for a_idx in range(n):
    if b_idx < n and a_card[a_idx] > b_card[b_idx]:
        answer += 1
        b_idx += 1
print(answer)