n,k = map(int,input().split())

arr = [0 for _ in range(k)]
for i in range(n):
    arr.append(int(input()))

for i in range(k):
    arr.append(0)

#print(arr)

boom = []

for i in range(k,k+n):
    for j in range(i+1,i+k):
        if arr[i] == arr[j]:
            boom.append(arr[i])
print(max(boom))