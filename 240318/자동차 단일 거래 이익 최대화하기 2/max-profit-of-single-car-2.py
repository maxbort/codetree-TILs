import sys

input = sys.stdin.readline

n = int(input())

car_price = list(map(int,input().split()))

answer= 0
for i in range(n-1):
    for j in range(i+1,n):
        tmp = car_price[j] - car_price[i]
        answer = max(tmp,answer)

print(answer)