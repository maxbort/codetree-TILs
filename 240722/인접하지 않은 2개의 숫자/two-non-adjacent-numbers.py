n = int(input())

arr = list(map(int,input().split()))

max_val = 0

for i in range(n):
    val = arr[i]
    for j in range(i+2, n):
        val += arr[j]
        max_val = max(max_val, val)
        val -= arr[j]
print(max_val)