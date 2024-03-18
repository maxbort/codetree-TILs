import sys

input = sys.stdin.readline

n = int(input())

word = {}

for _ in range(n):
    a = str(input().rstrip())
    if a not in word:
        word[a] = 1
    else:
        word[a] += 1
max_cnt = max(word.values())

print(max_cnt)