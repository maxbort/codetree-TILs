n = int(input())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

temp = [0 for _ in range(101)]

for x,y in arr:
    for i in range(x,y+1):
        temp[i] += 1
print(max(temp))