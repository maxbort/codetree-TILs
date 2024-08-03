n = int(input())

arr = [
    int(input())
    for _ in range(n)
]


if n == 1:
    print(1)
else:
    max_cnt = 0
    cnt = 1
    for i in range(1,n):
        if arr[i] == arr[i-1]:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
    max_cnt = max(max_cnt, cnt)
        

    print(max_cnt)