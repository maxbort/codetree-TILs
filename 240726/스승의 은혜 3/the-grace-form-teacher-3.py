n,b = map(int,input().split())

price = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_val = 0

for i in range(n):
    val = 0
    temp = b
    price[i][0] //= 2

    price.sort(key=lambda x : (x[0] + x[1]))

    for j in range(n):

        if temp - price[j][0] - price[j][1] >= 0:
            val += 1
            temp = temp - price[j][0] - price[j][1]
    
    max_val = max(max_val, val)
    price[i][0] *= 2

print(max_val)