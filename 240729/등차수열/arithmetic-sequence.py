n = int(input())
arr = list(map(int,input().split()))

cnt = 0
for k in range(1,51):
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[j]  - k == k - arr[i]:
                cnt += 1
print(cnt)