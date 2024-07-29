n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

max_cnt = 0
height = 0
for h in range(1,1001):

    if arr[0] - h > 0:
        cnt = 1
        flag = True
    else:
        cnt = 0
        flag = False

    for i in range(1,n):
        if arr[i] - h > 0:
            if flag == True:
                continue
            else:
                flag = True
                cnt += 1
                
    if max_cnt <= cnt:
        max_cnt = cnt
        height = h

print(height)