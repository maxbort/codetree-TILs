n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

if n == 1:
    print(1)
else:
    cnt = 1
    cur_val = arr[0]
    max_cnt = 0
    for i in range(1,n):
        if cur_val * arr[i] > 0:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
            cur_val = arr[i]
        max_cnt = max(max_cnt, cnt)
    print(max_cnt)