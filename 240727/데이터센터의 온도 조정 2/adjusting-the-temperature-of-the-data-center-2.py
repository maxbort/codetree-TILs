n,c,g,h = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

max_val = 0

temp = [0] * 1001

for i in range(1,1001):
    cnt = 0
    for j in range(n):
        if i < arr[j][0]:
            cnt += c
        elif arr[j][0] <= i <= arr[j][1]:
            cnt += g
        else:
            cnt += h
    
    max_val = max(max_val, cnt)

print(max_val)