import sys

input = sys.stdin.readline

n = int(input())
b_card = [int(input()) for _ in range(n)]

a_card = [i+1 for i in range(2*n)]

answer = 0
for i in b_card:
    if i < 2*n-1:
        if a_card[i+1] != 0:
            a_card[i+1] == 0
            answer += 1

print(answer)