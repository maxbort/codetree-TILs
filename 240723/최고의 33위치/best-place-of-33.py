n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def getSize(x,y):
    size = 0
    for a in range(x,x+3):
        for b in range(y,y+3):
            size += arr[a][b]
    return size

max_val = 0
for i in range(n-2):
    for j in range(n-2):
        max_val = max(max_val, getSize(i,j))
print(max_val)