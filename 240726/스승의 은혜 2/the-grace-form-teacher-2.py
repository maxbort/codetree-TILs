n,b = map(int,input().split())

price = [
    int(input())
    for _ in range(n)
]

max_val = 0

price.sort()

for i in range(n):
    val = 0
    temp = b
    price[i] //= 2

    for j in range(n):

        if temp - price[j] >= 0:
            val += 1
            temp -= price[j]
    
    max_val = max(max_val, val)
    price[i] *= 2

print(max_val)