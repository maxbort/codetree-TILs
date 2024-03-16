import sys
input = sys.stdin.readline

n, total = map(int,input().split())
coin = [int(input()) for _ in range(n)]

coin.sort(reverse=True)
answer= 0 
for i in coin:
    if i <= total:
        a = total//i
        total -= i *a
        answer += a
    if total <= 0:
        break
print(answer)