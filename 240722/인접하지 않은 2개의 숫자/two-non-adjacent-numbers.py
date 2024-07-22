n = int(input())

arr = list(map(int,input().split()))

max_val = 0

for i in range(n):
    cnt = arr[i]
    if i == 0:
        cnt += max(arr[2:])
    elif i == n-1:
        cnt += max(arr[:-2])
    else:
        for j in range(1,n-1):
            cnt = arr[i]
            if abs(i-j) >= 2:
                cnt += arr[j]
            max_val = max(max_val, cnt)
    
    max_val = max(max_val, cnt)
print(max_val)