n,m,c = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_val = 0
ans = []

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def possible(x1,y1,x2,y2):
    
    if y1 + m - 1 >= n or y2 + m - 1 >= n:
        return False

    if x1 != x2:
        return True
    
    if interact(y1, y1+m-1, y2, y2+m-1):
        return False
    return True

def interact(a,b,c,d):
    return not (b < c or d < a)

def choose(idx, weight, value):
    global max_val

    if idx == m:
        if weight <= c:
            max_val = max(max_val, value)
        return 
    
    choose(idx+1, weight, value)
    choose(idx+1, weight + ans[idx], value + ans[idx]** 2)

def find_max(x,y):
    global ans, max_val

    max_val = 0
    ans = arr[x][y:y+m]
    choose(0,0,0)

    return max_val


for i in range(n):
    for j in range(n):
        for x in range(n):
            for y in range(n):
                if possible(i,j,x,y):
                    max_val = max(max_val, find_max(i,j) + find_max(x,y))
print(max_val)