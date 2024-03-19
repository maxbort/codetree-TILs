import sys

input = sys.stdin.readline

word = input().rstrip()

cnt = {}
for i in word:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in word:
    if cnt[i] == 1:
        print(i)
        sys.exit()
print("None")