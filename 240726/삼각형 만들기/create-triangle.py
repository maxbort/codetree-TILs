n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_val = 0

def possible(a,b,c):
    x1, y1 = arr[a]
    x2, y2 = arr[b]
    x3, y3 = arr[c]

    if ((x1 == x2) and (x2 != x3)) and ((y3 == y1) or (y3 == y2)):
        return True

    if ((x1 == x3) and (x2 != x3)) and ((y2 == y1) or (y3 == y2)):
        return True
    
    if ((x2 == x3) and (x1 != x3)) and ((y2 == y1) or (y3 == y1)):
        return True

    return False

def calc(a,b,c):
    x1, y1 = arr[a]
    x2, y2 = arr[b]
    x3, y3 = arr[c]

    return abs(((x2 * y1) + (x3 * y2) + (x1 * y3)) - ((x1 * y2) + (x2 * y3) + (x3 * y1)))

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if possible(i,j,k):
                max_val = max(max_val, calc(i,j,k))
print(max_val)