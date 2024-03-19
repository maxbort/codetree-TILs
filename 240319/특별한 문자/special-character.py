import sys

input = sys.stdin.readline

word = input().rstrip()

for i in word:
    if word.count(i) == 1:
        print(i)
        sys.exit()
print("None")