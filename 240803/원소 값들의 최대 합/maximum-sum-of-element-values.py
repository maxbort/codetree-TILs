n,m = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort(reverse=True)

cnt = 0
for i in range(m):
    cnt += arr[i]
print(cnt)