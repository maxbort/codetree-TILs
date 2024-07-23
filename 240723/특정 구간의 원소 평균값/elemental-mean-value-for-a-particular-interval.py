n = int(input())
arr = list(map(int,input().split()))

cnt = 0

for i in range(n):
    for j in range(i, n):
        val = 0
        for k in range(i,j+1):
            val += arr[k]
        
        if i == j:
            avg = val
        else:
            avg = val / abs(j-i)

        if avg in arr[i:j+1]:
            cnt += 1
print(cnt)