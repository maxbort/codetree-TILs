n,m = map(int,input().split())
arr = [0] + list(map(int,input().split()))

max_cnt = 0
for i in range(1,n+1):
    cnt = arr[i]
    idx = arr[i]
    for _ in range(m-1):
        cnt += arr[idx]
        idx = arr[idx]
    max_cnt = max(max_cnt, cnt)
print(max_cnt)