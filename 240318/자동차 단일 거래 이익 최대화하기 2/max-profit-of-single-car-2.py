import sys

input = sys.stdin.readline

n = int(input())

car_price = list(map(int,input().split()))

answer = 0
min_price = car_price[0]

for i in range(n):
    tmp = car_price[i] - min_price

    answer = max(answer,tmp)

    if min_price > car_price[i]:
        min_price = car_price[i]
print(answer)