import sys

input = sys.stdin.readline

n = list(map(int,input().rstrip()))

check = 1
length = len(n)
for i in range(length):
    if n[i] == 0:
        n[i] = 1
        check = 0
        break

if check == 1:
    for i in range(length,-1):
        if n[i] == 1:
            n[i] = 0
            break
answer = 0
length -= 1
for i in n:
    answer += i * (2**length)
    length-=1
print(answer)