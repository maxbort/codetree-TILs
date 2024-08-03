n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

max_cnt = 0
cnt = 1
for i in range(1,n):
    if arr[i] == arr[i-1]:
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)
        cnt = 1
    

print(max_cnt)