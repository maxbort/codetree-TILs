n,b = map(int,input().split())

price = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_val = 0


for i in range(n):
    val = 0
    temp = b
    temp_arr = [item[:] for item in price]
    temp_arr[i][0] //= 2
    temp_arr.sort(key=lambda x : (x[0] + x[1]))

    for j in range(n):

        if temp - sum(temp_arr[j]) >= 0:
            val += 1
            temp -= sum(temp_arr[j])
    
    max_val = max(max_val, val)
    
print(max_val)