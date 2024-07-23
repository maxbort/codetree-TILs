n,k = map(int,input().split())
arr = list(map(int,input().split()))


max_val = 0
for i in range(n-k+1):
    cnt = 0
    for j in range(i,i+k):
        cnt += arr[j]
    
    max_val = max(max_val, cnt)
print(max_val)