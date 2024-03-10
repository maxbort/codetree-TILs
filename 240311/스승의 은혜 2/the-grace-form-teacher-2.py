import sys

input = sys.stdin.readline

n,b = map(int,input().split())

price = [int(input()) for _ in range(n)]

price.sort()
answer = 0

tmp = 0
for i in price:
    tmp += i
    
    if tmp > b:
        tmp -= i
        half = i//2
        tmp += half
        if tmp > b:
            break
    answer += 1
print(answer)