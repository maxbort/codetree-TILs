n,k = map(int,input().split())

arr = [0 for _ in range(k)]
for i in range(n):
    arr.append(int(input()))

for i in range(k):
    arr.append(0)

boom = []

for i in range(n):
    for j in range(i+1,i+2*k):
        if arr[i] == arr[j]:
            boom.append(arr[i])
print(max(boom))